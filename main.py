
from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.responses import JSONResponse
from pydantic import EmailStr
import logging
from relatorio import processar_csv
from email_utils import enviar_email

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="API de Processamento CSV",
    description="API para processar arquivos CSV e enviar relatórios por email",
    version="1.0.0"
)

@app.get("/")
async def root():
    """Endpoint raiz da API"""
    return {"message": "API de Processamento CSV e Envio de Relatório por Email"}

@app.post("/enviar-relatorio/")
async def enviar_relatorio(
    arquivo: UploadFile = File(..., description="Arquivo CSV para processamento"),
    email_destino: EmailStr = Form(..., description="Email de destino para envio do relatório")
):
    """
    Processa um arquivo CSV e envia relatório por email
    
    Args:
        arquivo: Arquivo CSV para ser processado
        email_destino: Email para onde enviar o relatório
        
    Returns:
        Mensagem de sucesso ou erro
    """
    try:
        # Validar tipo de arquivo
        if not arquivo.filename.endswith('.csv'):
            raise HTTPException(
                status_code=400, 
                detail="Apenas arquivos CSV são aceitos"
            )
        
        # EmailStr já valida formato de email via Pydantic
        
        logger.info(f"Processando arquivo: {arquivo.filename}")
        
        # Ler e processar arquivo
        conteudo = await arquivo.read()
        if len(conteudo) == 0:
            raise HTTPException(
                status_code=400, 
                detail="Arquivo está vazio"
            )
        
        relatorio = processar_csv(conteudo)
        
        # Enviar email
        enviar_email(destinatario=email_destino, mensagem=relatorio)
        
        logger.info(f"Relatório enviado com sucesso para: {email_destino}")
        
        return JSONResponse(
            status_code=200,
            content={
                "mensagem": f"Relatório enviado com sucesso para {email_destino}",
                "arquivo_processado": arquivo.filename
            }
        )
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Erro no processamento: {str(e)}")
        raise HTTPException(
            status_code=500, 
            detail=f"Erro interno: {str(e)}"
        )

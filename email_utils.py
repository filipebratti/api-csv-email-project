
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
import logging
from dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger(__name__)

EMAIL_REMETENTE = os.getenv("EMAIL_REMETENTE")
SENHA_REMETENTE = os.getenv("SENHA_REMETENTE")

def verificar_configuracoes():
    """
    Verifica se as configurações de email estão definidas
    
    Raises:
        ValueError: Se as credenciais não estiverem configuradas
    """
    if not EMAIL_REMETENTE or not SENHA_REMETENTE:
        raise ValueError(
            "Credenciais de email não configuradas. "
            "Verifique o arquivo .env com EMAIL_REMETENTE e SENHA_REMETENTE"
        )

def enviar_email(destinatario: str, mensagem: str):
    """
    Envia um email com o relatório para o destinatário especificado
    
    Args:
        destinatario: Email do destinatário
        mensagem: Conteúdo do relatório a ser enviado
        
    Raises:
        ValueError: Se as credenciais não estiverem configuradas
        Exception: Se houver erro no envio do email
    """
    try:
        verificar_configuracoes()
        
        # Criar mensagem
        msg = MIMEMultipart()
        msg['Subject'] = "📊 Relatório de Análise de Dados CSV"
        msg['From'] = EMAIL_REMETENTE
        msg['To'] = destinatario
        
        # Adicionar corpo do email
        corpo_email = f"""
Olá!

Segue abaixo o relatório de análise dos dados do arquivo CSV processado.

{mensagem}

---
Este email foi enviado automaticamente pela API de Processamento CSV.
        """
        
        msg.attach(MIMEText(corpo_email, 'plain', 'utf-8'))
        
        # Enviar email
        logger.info(f"Tentando enviar email para: {destinatario}")
        
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(EMAIL_REMETENTE, SENHA_REMETENTE)
            server.send_message(msg)
            
        logger.info(f"Email enviado com sucesso para: {destinatario}")
        
    except smtplib.SMTPAuthenticationError:
        error_msg = "Erro de autenticação. Verifique as credenciais de email"
        logger.error(error_msg)
        raise Exception(error_msg)
    except smtplib.SMTPException as e:
        error_msg = f"Erro SMTP: {str(e)}"
        logger.error(error_msg)
        raise Exception(error_msg)
    except Exception as e:
        error_msg = f"Erro ao enviar email: {str(e)}"
        logger.error(error_msg)
        raise Exception(error_msg)



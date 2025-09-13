
import pandas as pd
from io import BytesIO
import logging

logger = logging.getLogger(__name__)

def processar_csv(conteudo: bytes) -> str:
    """
    Processa um arquivo CSV e gera um relatório estatístico
    
    Args:
        conteudo: Conteúdo do arquivo CSV em bytes
        
    Returns:
        String contendo o relatório formatado
        
    Raises:
        ValueError: Se o arquivo CSV não puder ser processado
    """
    try:
        # Ler CSV
        df = pd.read_csv(BytesIO(conteudo))
        
        if df.empty:
            raise ValueError("Arquivo CSV está vazio ou não possui dados válidos")
        
        logger.info(f"CSV processado com sucesso. Linhas: {len(df)}, Colunas: {len(df.columns)}")
        
        # Gerar relatório
        relatorio_partes = []
        relatorio_partes.append("=" * 50)
        relatorio_partes.append("RELATÓRIO DE ANÁLISE DE DADOS")
        relatorio_partes.append("=" * 50)
        relatorio_partes.append(f"\n📊 INFORMAÇÕES GERAIS:")
        relatorio_partes.append(f"   • Total de registros: {len(df)}")
        relatorio_partes.append(f"   • Total de colunas: {len(df.columns)}")
        relatorio_partes.append(f"   • Colunas: {', '.join(df.columns)}")
        
        # Estatísticas descritivas para colunas numéricas
        colunas_numericas = df.select_dtypes(include=['number']).columns
        if len(colunas_numericas) > 0:
            relatorio_partes.append(f"\n📈 ESTATÍSTICAS DESCRITIVAS:")
            resumo = df[colunas_numericas].describe()
            relatorio_partes.append(resumo.to_string())
        
        # Informações sobre valores ausentes
        valores_ausentes = df.isnull().sum()
        if valores_ausentes.sum() > 0:
            relatorio_partes.append(f"\n⚠️  VALORES AUSENTES:")
            for col, count in valores_ausentes.items():
                if count > 0:
                    relatorio_partes.append(f"   • {col}: {count} valores ausentes")
        else:
            relatorio_partes.append(f"\n✅ Nenhum valor ausente encontrado")
        
        # Primeiras linhas do dataset
        relatorio_partes.append(f"\n📋 AMOSTRA DOS DADOS (primeiras 5 linhas):")
        relatorio_partes.append(df.head().to_string())
        
        relatorio_partes.append("\n" + "=" * 50)
        
        return "\n".join(relatorio_partes)
        
    except pd.errors.EmptyDataError:
        raise ValueError("Arquivo CSV está vazio")
    except pd.errors.ParserError as e:
        raise ValueError(f"Erro ao processar CSV: {str(e)}")
    except Exception as e:
        logger.error(f"Erro no processamento do CSV: {str(e)}")
        raise ValueError(f"Erro inesperado no processamento: {str(e)}")

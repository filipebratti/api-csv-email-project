
# API de Processamento de CSV + Envio de Relatório por E-mail

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green.svg)](https://fastapi.tiangolo.com)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Uma API REST moderna construída com **FastAPI** que:
1. 📁 Recebe um arquivo CSV via upload
2. 🔍 Processa os dados com **Pandas**
3. 📈 Gera um relatório estatístico detalhado
4. 📧 Envia o relatório por e-mail automaticamente

## ✨ Funcionalidades

- ✅ **Upload de arquivos CSV** com validação
- ✅ **Análise estatística completa** dos dados
- ✅ **Envio automático por email** com relatórios formatados
- ✅ **Tratamento de erros** robusto
- ✅ **Logging** para debugging
- ✅ **Documentação interativa** com Swagger UI
- ✅ **Validações de entrada** (formato de email, tipo de arquivo)

## 🚀 Demo

![API Demo](https://via.placeholder.com/800x400?text=API+Demo+Screenshot)

## 📋 Requisitos

- **Python 3.9+**
- **pip** funcionando corretamente
- **Conta Gmail** com senha de app configurada

## �️ Instalação

### 1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/projeto_api_csv_email.git
cd projeto_api_csv_email
```

### 2. Instale as dependências
```bash
pip install -r requirements.txt
```

### 3. Configure as credenciais de email
Copie o arquivo de exemplo e configure suas credenciais:
```bash
cp .env.example .env
```

Edite o arquivo `.env` com suas credenciais:
```env
EMAIL_REMETENTE=seu_email@gmail.com
SENHA_REMETENTE=sua_senha_de_app_16_digitos
```

## ⚙️ Configuração do Gmail

### 🔐 Como gerar uma senha de app:

1. Acesse: [Google App Passwords](https://myaccount.google.com/apppasswords)
2. Faça login com sua conta Gmail
3. Selecione **"Outro (personalizado)"** e digite `API-CSV`
4. Clique em **"Gerar"**
5. Copie a **senha de 16 dígitos** gerada
6. Use essa senha no arquivo `.env`

## 🏃‍♂️ Executando a API

```bash
python -m uvicorn main:app --reload
```

A API estará disponível em: **http://127.0.0.1:8000**

## 📖 Documentação da API

Acesse a documentação interativa em:
- **Swagger UI**: http://127.0.0.1:8000/docs
- **ReDoc**: http://127.0.0.1:8000/redoc

## 💡 Como Usar

### 1. Via Interface Web (Swagger UI)
1. Acesse http://127.0.0.1:8000/docs
2. Clique em **"POST /enviar-relatorio/"**
3. Clique em **"Try it out"**
4. Faça upload do arquivo CSV
5. Digite o email de destino
6. Clique em **"Execute"**

### 2. Via cURL
```bash
curl -X POST "http://127.0.0.1:8000/enviar-relatorio/" \
  -H "Content-Type: multipart/form-data" \
  -F "arquivo=@exemplo.csv" \
  -F "email_destino=destinatario@email.com"
```

### 3. Via Python
```python
import requests

with open('exemplo.csv', 'rb') as f:
    files = {'arquivo': f}
    data = {'email_destino': 'destinatario@email.com'}
    response = requests.post('http://127.0.0.1:8000/enviar-relatorio/', 
                           files=files, data=data)
    print(response.json())
```

## � Estrutura do Projeto

```
projeto_api_csv_email/
│
├── 📄 main.py              # API FastAPI principal
├── 📊 relatorio.py         # Processamento e análise do CSV  
├── 📧 email_utils.py       # Utilitários para envio de email
├── 📋 exemplo.csv          # Arquivo de exemplo para teste
├── ⚙️  requirements.txt    # Dependências do projeto
├── 🔒 .env.example         # Exemplo de configuração
├── 🚫 .gitignore           # Arquivos ignorados pelo Git
└── 📖 README.md            # Esta documentação
```

## 🧪 Exemplo de Relatório

O relatório gerado inclui:

```
==================================================
RELATÓRIO DE ANÁLISE DE DADOS
==================================================

📊 INFORMAÇÕES GERAIS:
   • Total de registros: 3
   • Total de colunas: 3
   • Colunas: nome, idade, salario

📈 ESTATÍSTICAS DESCRITIVAS:
              idade       salario
count      3.000000      3.000000
mean      30.000000   5500.000000
std        5.000000   1322.875656
min       25.000000   4500.000000
25%       27.500000   4750.000000
50%       30.000000   5000.000000
75%       32.500000   6000.000000
max       35.000000   7000.000000

✅ Nenhum valor ausente encontrado

📋 AMOSTRA DOS DADOS (primeiras 5 linhas):
    nome  idade  salario
0  Alice     30     5000
1    Bob     25     4500
2  Carol     35     7000
==================================================
```

## 🛡️ Tratamento de Erros

A API inclui tratamento robusto para:
- ❌ **Arquivos não-CSV**: Rejeita arquivos que não sejam .csv
- ❌ **Arquivos vazios**: Valida se o arquivo contém dados
- ❌ **Emails inválidos**: Verifica formato básico de email
- ❌ **Credenciais inválidas**: Trata erros de autenticação SMTP
- ❌ **CSVs malformados**: Captura erros de parsing do Pandas

## 🤝 Contribuindo

1. Fork o projeto
2. Crie sua feature branch (`git checkout -b feature/MinhaFeature`)
3. Commit suas mudanças (`git commit -m 'Adiciona MinhaFeature'`)
4. Push para a branch (`git push origin feature/MinhaFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para detalhes.

## ⭐ Mostre seu apoio

Se este projeto foi útil para você, deixe uma ⭐!

---

<div align="center">
Feito com ❤️ usando FastAPI e Python
</div>



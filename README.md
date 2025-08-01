# Cotação API

Este projeto consulta a cotação do dólar em relação ao real utilizando a API ExchangeRate. O script [`consulta.py`](consulta.py) faz uma requisição à API e exibe o valor de 1 dólar em reais.

## Pré-requisitos

- Python instalado
- Ambiente virtual configurado (recomendado)
- Chave de API da ExchangeRate (já incluída no arquivo `.env`)

## Passo a passo para executar

1. **Clone o repositório ou baixe os arquivos do projeto.**

2. **Crie e ative o ambiente virtual (opcional, mas recomendado):**
   ```sh
   python -m venv venv_SEU-NOME
   # Para ativar no Windows:
   venv_SEU-NOME\Scripts\activate
   ```

3. **Instale as dependências:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Configure o arquivo `.env` (crie um caso necessário) com sua chave de API:**
   ```env
   # .env

   API_KEY=<SUA_CHAVE>
   ```

5. **Execute o script `consulta.py`:**
   ```sh
   python consulta.py
   ```   

O resultado será exibido no terminal, mostrando o valor de 1 dólar em reais.


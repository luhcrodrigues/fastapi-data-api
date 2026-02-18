# Imagem base leve do Python

FROM python:3.12-slim
# Diretório interno do container

WORKDIR /app
# Copia primeiro o requirements (aproveita cache do Docker)

COPY requirements.txt .
# Instala dependências

RUN pip install --no-cache-dir -r requirements.txt
# Copia o restante do projeto

COPY . .
# Executa a aplicação
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

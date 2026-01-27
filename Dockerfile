FROM python:3.11-slim

# Diretório de trabalho dentro do container
WORKDIR /app

# Copia dependências
COPY requirements.txt .

# Instala dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia o código da API
COPY app/main.py .


# Expõe a porta da API
EXPOSE 8000

# Comando para rodar a API
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

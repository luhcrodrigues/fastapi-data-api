import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
# Carrega variáveis do arquivo .env
load_dotenv()

# Lê a variável de ambiente do banco
DATABASE_URL = os.getenv("DATABASE_URL")
# Cria o engine (conexão principal com o banco)
engine = create_engine(DATABASE_URL)
# Fábrica de sessões (conexões individuais)
SessionLocal = sessionmaker(
    autocommit=False, # Controle manual de transação
    autoflush=False,# Evita gravações automáticas inesperadas
    bind=engine
)
# Base declarativa para modelos ORM

Base = declarative_base()

def get_db():
    """
    Dependency Injection usada nos endpoints.
    Garante que a sessão sempre será fechada.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
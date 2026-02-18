from sqlalchemy import Column, Integer, String, Date, Float, DateTime
from datetime import datetime
from app.database import Base

class Production(Base):
    """
    Modelo ORM da tabela 'productions'.
    Representa os dados persistidos no banco.
    """

    __tablename__ = "productions"  # Nome explícito da tabela

    # Chave primária com index para melhorar performance de busca
    id = Column(Integer, primary_key=True, index=True)

    # Dados operacionais
    date = Column(Date, nullable=False)   # Data da produção
    line = Column(String, nullable=False) # Linha de produção
    area = Column(String, nullable=False) # Área operacional

    # Indicadores produtivos
    capacity = Column(Float, nullable=False)
    produced_quantity = Column(Float, nullable=False)
    available_capacity = Column(Float, nullable=False)

    # Campo de auditoria automático
    created_at = Column(DateTime, default=datetime.utcnow)
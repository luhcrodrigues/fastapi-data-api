from sqlalchemy import Column, Integer, String, Date, Float, DateTime
from datetime import datetime
from app.database import Base

class Production(Base):
    __tablename__ = "productions"

    id = Column(Integer, primary_key=True, index=True)

    date = Column(Date, nullable=False)
    line = Column(String, nullable=False)
    area = Column(String, nullable=False)

    capacity = Column(Float, nullable=False)
    produced_quantity = Column(Float, nullable=False)
    available_capacity = Column(Float, nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow)

"""
Script para popular o banco com dados fictícios
para testes e demonstração.
"""


from app.database import SessionLocal
from app.models.production import Production
from datetime import date, timedelta
import random

db = SessionLocal()

linhas = ["LA", "LT", "LCA"]
areas = ["BQ1", "BQ2", "BQ3"]

dados = []

data_base = date(2026, 2, 1)

for i in range(30):
    nova_data = data_base + timedelta(days=i)

    capacity = random.choice([1000, 1200, 1500])
    produced = random.randint(int(capacity * 0.7), capacity)
    available = capacity - random.randint(0, 100)

    prod = Production(
        date=nova_data,
        line=random.choice(linhas),
        area=random.choice(areas),
        capacity=capacity,
        produced_quantity=produced,
        available_capacity=available
    )

    dados.append(prod)
    
# Inserção em lote
db.add_all(dados)
db.commit()
db.close()

print("30 registros inseridos com sucesso ")

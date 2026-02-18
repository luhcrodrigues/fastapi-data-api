from sqlalchemy.orm import Session
from app.models.production import Production
from app.schemas.production import ProductionCreate

# ==============================
# CRIAÇÃO DE REGISTROS DE PRODUÇÃO
# ==============================

def create_production(db: Session, production: ProductionCreate):
    """
    Cria um novo registro de produção no banco de dados.

    - Converte o schema (Pydantic) em dicionário
    - Instancia o modelo ORM
    - Persiste no banco
    - Retorna o objeto atualizado com ID gerado
    """
    db_production = Production(**production.model_dump())

    db.add(db_production)       # Adiciona à sessão
    db.commit()                 # Confirma transação
    db.refresh(db_production)   # Atualiza objeto com dados do banco (ex: id)

    return db_production
# ==============================
# LEITURA (Lista com Paginação)
# ==============================

def get_productions(db: Session, skip: int = 0, limit: int = 10):
    """
    Retorna lista paginada de produções.

    skip - quantidade de registros ignorados
    limit - quantidade máxima retornada
    """
    return db.query(Production).offset(skip).limit(limit).all()


def count_productions(db: Session):
    """
    Retorna total de registros na tabela.
    Utilizado para paginação.
    """
    return db.query(Production).count()

# ==============================
# LEITURA (Por ID)
# ==============================

def get_production_by_id(db: Session, production_id: int):
    """
    Busca um registro pelo ID.
    Retorna None se não existir.
    """
    return db.query(Production).filter(Production.id == production_id).first()

# ==============================
# ATUALIZAÇÃO
# ==============================

def update_production(db: Session, production_id: int, production_data):
    """
    Atualiza um registro de produção existente.

    - Busca o registro pelo ID
    - Atualiza os campos com os dados fornecidos
    - Persiste as alterações no banco
    - Retorna o objeto atualizado ou None se não existir
    """
    production = db.query(Production).filter(Production.id == production_id).first()

    if not production:
        return None
  # Atualização dinâmica dos campos
    for key, value in production_data.model_dump().items():
        setattr(production, key, value)

    db.commit()
    db.refresh(production)

    return production

# ==============================
# DELETE
# ==============================
def delete_production(db: Session, production_id: int):
    """
    Remove um registro de produção existente.

    - Busca o registro pelo ID
    - Remove do banco
    - Retorna o objeto removido ou None se não existir
    """
    production = db.query(Production).filter(Production.id == production_id).first()

    if not production:
        return None

    db.delete(production)
    db.commit()

    return production

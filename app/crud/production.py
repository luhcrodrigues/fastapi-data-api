from sqlalchemy.orm import Session
from app.models.production import Production
from app.schemas.production import ProductionCreate

def create_production(db: Session, production: ProductionCreate):
    db_production = Production(**production.model_dump())
    db.add(db_production)
    db.commit()
    db.refresh(db_production)
    return db_production

def get_productions(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Production).offset(skip).limit(limit).all()

def count_productions(db: Session):
    return db.query(Production).count()
def get_production_by_id(db: Session, production_id: int):
    return db.query(Production).filter(Production.id == production_id).first()
def update_production(db: Session, production_id: int, production_data):
    production = db.query(Production).filter(Production.id == production_id).first()

    if not production:
        return None

    for key, value in production_data.model_dump().items():
        setattr(production, key, value)

    db.commit()
    db.refresh(production)

    return production


def delete_production(db: Session, production_id: int):
    production = db.query(Production).filter(Production.id == production_id).first()

    if not production:
        return None

    db.delete(production)
    db.commit()

    return production

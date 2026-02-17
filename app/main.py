from fastapi import FastAPI, Depends, Query
from sqlalchemy.orm import Session

from app.database import Base, engine, get_db
from app.models import production  # IMPORTANTE para criar tabela
from app.schemas.production import ProductionCreate, ProductionResponse
from app.crud import production as production_crud
from fastapi import HTTPException
from app.schemas.production import ProductionUpdate

app = FastAPI()

# Cria as tabelas automaticamente
Base.metadata.create_all(bind=engine)


from fastapi.responses import RedirectResponse

@app.get("/", include_in_schema=False)
def root():
    return RedirectResponse(url="/docs")



@app.post("/v1/production", response_model=ProductionResponse)
def create_production(
    production: ProductionCreate,
    db: Session = Depends(get_db)
):
    return production_crud.create_production(db, production)


@app.get("/v1/production")
def list_productions(
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1),
    db: Session = Depends(get_db)
):
    skip = (page - 1) * limit
    data = production_crud.get_productions(db, skip=skip, limit=limit)
    total = production_crud.count_productions(db)

    return {
        "total": total,
        "page": page,
        "limit": limit,
        "data": data
    }
@app.get("/v1/production/{production_id}", response_model=ProductionResponse)
def get_production(
    production_id: int,
    db: Session = Depends(get_db)
):
    production = production_crud.get_production_by_id(db, production_id)

    if not production:
        raise HTTPException(status_code=404, detail="Production not found")

    return production
from app.schemas.production import ProductionUpdate

@app.put("/v1/production/{production_id}", response_model=ProductionResponse)
def update_production(
    production_id: int,
    production: ProductionUpdate,
    db: Session = Depends(get_db)
):
    updated = production_crud.update_production(db, production_id, production)

    if not updated:
        raise HTTPException(status_code=404, detail="Production not found")

    return updated
@app.delete("/v1/production/{production_id}")
def delete_production(
    production_id: int,
    db: Session = Depends(get_db)
):
    deleted = production_crud.delete_production(db, production_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Production not found")

    return {"message": "Production deleted successfully"}

# ==============================
# IMPORTAÇÕES
# ==============================

# Componentes principais do FastAPI
from fastapi import FastAPI, Depends, Query, HTTPException

# Para redirecionar automaticamente a rota raiz
from fastapi.responses import RedirectResponse

# Tipo da sessão do SQLAlchemy
from sqlalchemy.orm import Session

# Configuração de banco
from app.database import Base, engine, get_db

# IMPORTANTE:
# Esse import força o SQLAlchemy a registrar o model
# antes da criação automática das tabelas
from app.models import production

# Schemas Pydantic (validação e resposta)
from app.schemas.production import (
    ProductionCreate,
    ProductionResponse,
    ProductionUpdate
)

# Camada CRUD (acesso ao banco)
from app.crud import production as production_crud


# ==============================
# CONFIGURAÇÃO DO SWAGGER
# ==============================

# Organização visual das rotas no Swagger
tags_metadata = [
    {
        "name": "Production",
        "description": "Operações relacionadas aos KPIs de produção industrial."
    },
    {
        "name": "System",
        "description": "Verificações e status do sistema."
    }
]

# Criação da aplicação FastAPI
app = FastAPI(
    title="Data API",
    description="""
## API Data

Microserviço desenvolvido para gerenciamento de dados de produção industrial.

### Funcionalidades
- CRUD completo de produção
- Paginação de resultados
- Persistência em PostgreSQL
- Containerização com Docker
- Estrutura modular com boas práticas REST
""",
    version="1.0.0",
    contact={
        "name": "Luana Rodrigues",
        "email": "suporte@empresa.com"
    },
    openapi_tags=tags_metadata
)


# ==============================
# CRIAÇÃO AUTOMÁTICA DAS TABELAS
# ==============================

# Lê todos os models registrados e cria as tabelas
# caso ainda não existam no banco
Base.metadata.create_all(bind=engine)


# ==============================
# ROTA RAIZ
# ==============================

# Quando acessar http://localhost:8000
# redireciona automaticamente para o Swagger
@app.get("/", include_in_schema=False)
def root():
    return RedirectResponse(url="/docs")


# ==============================
# CRUD DE PRODUÇÃO
# ==============================


# ------------------------------
# CREATE
# ------------------------------

@app.post(
    "/v1/production",
    response_model=ProductionResponse,
    tags=["Production"],
    summary="Criar registro de produção"
)
def create_production(
    production: ProductionCreate,           # Dados validados pelo Pydantic
    db: Session = Depends(get_db)           # Injeção automática da sessão
):
    # Delegação para camada CRUD
    return production_crud.create_production(db, production)


# ------------------------------
# READ (LISTAGEM COM PAGINAÇÃO)
# ------------------------------

@app.get(
    "/v1/production",
    tags=["Production"],
    summary="Listar produções com paginação"
)
def list_productions(
    page: int = Query(1, ge=1),             # Página mínima = 1
    limit: int = Query(10, ge=1),           # Limite mínimo = 1
    db: Session = Depends(get_db)
):
    # Fórmula da paginação:
    # skip = (pagina - 1) * limite
    skip = (page - 1) * limit

    # Busca dados paginados
    data = production_crud.get_productions(db, skip=skip, limit=limit)

    # Conta total de registros
    total = production_crud.count_productions(db)

    # Retorno estruturado padrão enterprise
    return {
        "total": total,
        "page": page,
        "limit": limit,
        "data": data
    }


# ------------------------------
# READ (BUSCA POR ID)
# ------------------------------

@app.get(
    "/v1/production/{production_id}",
    response_model=ProductionResponse,
    tags=["Production"],
    summary="Buscar produção por ID"
)
def get_production(
    production_id: int,
    db: Session = Depends(get_db)
):
    production = production_crud.get_production_by_id(db, production_id)

    # Tratamento de erro HTTP
    if not production:
        raise HTTPException(status_code=404, detail="Production not found")

    return production


# ------------------------------
# UPDATE
# ------------------------------

@app.put(
    "/v1/production/{production_id}",
    response_model=ProductionResponse,
    tags=["Production"],
    summary="Atualizar produção"
)
def update_production(
    production_id: int,
    production: ProductionUpdate,
    db: Session = Depends(get_db)
):
    updated = production_crud.update_production(db, production_id, production)

    # Se o ID não existir, retorna erro 404
    if not updated:
        raise HTTPException(status_code=404, detail="Production not found")

    return updated


# ------------------------------
# DELETE
# ------------------------------

@app.delete(
    "/v1/production/{production_id}",
    tags=["Production"],
    summary="Remover produção"
)
def delete_production(
    production_id: int,
    db: Session = Depends(get_db)
):
    deleted = production_crud.delete_production(db, production_id)

    # Tratamento de erro se não existir
    if not deleted:
        raise HTTPException(status_code=404, detail="Production not found")

    return {"message": "Production deleted successfully"}

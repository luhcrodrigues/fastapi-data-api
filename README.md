# FastAPI Data API - Industrial Production

API REST para gerenciamento de dados de produção industrial, desenvolvida com FastAPI, PostgreSQL e Docker.

## Tecnologias

- **Python 3.12**
- **FastAPI** - Framework web
- **SQLAlchemy** - ORM para banco de dados
- **PostgreSQL 15** - Banco de dados
- **Docker / Docker Compose** - Containerização
- **Pydantic** - Validação de dados
- **Uvicorn** - Servidor ASGI

## Estrutura do Projeto

```
fastapi-data-api/
├── app/
│   ├── main.py          # Rotas e configuração da aplicação
│   ├── database.py      # Conexão com o banco de dados
│   ├── models/
│   │   └── production.py    # Model da tabela productions
│   ├── schemas/
│   │   └── production.py    # Schemas Pydantic (validação)
│   └── crud/
│       └── production.py    # Operações no banco de dados
├── seed/
│   └── seed_more.py     # Script para popular o banco com dados
├── Dockerfile
├── docker-compose.yml
└── requirements.txt
```

## Como rodar o projeto

### Pré-requisitos

- [Docker](https://www.docker.com/) instalado
- [Docker Compose](https://docs.docker.com/compose/) instalado

### 1. Clone o repositório

```bash
git clone <url-do-repositorio>
cd fastapi-data-api
```

### 2. Crie o arquivo `.env`

```bash
DATABASE_URL=postgresql://postgres:postgres@db:5432/industrial_db
```

### 3. Suba os containers

```bash
docker-compose up --build
```

### 4. Acesse a documentação

Após subir, acesse no navegador:

```
http://localhost:8000/docs
```

A rota `/` já redireciona automaticamente para a documentação Swagger.

---

## Endpoints

Base URL: `http://localhost:8000/v1`

| Metodo | Rota | Descricao |
|--------|------|-----------|
| `POST` | `/v1/production` | Criar novo registro de producao |
| `GET` | `/v1/production` | Listar producoes com paginacao |
| `GET` | `/v1/production/{id}` | Buscar producao por ID |
| `PUT` | `/v1/production/{id}` | Atualizar producao |
| `DELETE` | `/v1/production/{id}` | Deletar producao |

### Parametros de paginacao (GET /v1/production)

| Parametro | Tipo | Padrao | Descricao |
|-----------|------|--------|-----------|
| `page` | int | 1 | Numero da pagina |
| `limit` | int | 10 | Itens por pagina |

### Exemplo de payload (POST / PUT)

```json
{
  "date": "2024-01-15",
  "line": "Linha A",
  "area": "Setor 1",
  "capacity": 1000.0,
  "produced_quantity": 850.0,
  "available_capacity": 150.0
}
```

### Exemplo de resposta (GET /v1/production)

```json
{
  "total": 50,
  "page": 1,
  "limit": 10,
  "data": [
    {
      "id": 1,
      "date": "2024-01-15",
      "line": "Linha A",
      "area": "Setor 1",
      "capacity": 1000.0,
      "produced_quantity": 850.0,
      "available_capacity": 150.0
    }
  ]
}
```

---

## Model de Producao

| Campo | Tipo | Descricao |
|-------|------|-----------|
| `id` | int | ID unico (gerado automaticamente) |
| `date` | date | Data da producao |
| `line` | string | Linha de producao |
| `area` | string | Area/setor |
| `capacity` | float | Capacidade total |
| `produced_quantity` | float | Quantidade produzida |
| `available_capacity` | float | Capacidade disponivel |
| `created_at` | datetime | Data de criacao do registro |

---

## Fluxo de Branches (Git Flow)

```
feature/  →  dev  →  master
```

- `feature/` - Desenvolvimento de novas funcionalidades
- `dev` - Ambiente de desenvolvimento e testes
- `master` - Producao
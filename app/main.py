from fastapi import FastAPI

app = FastAPI(
    title="Data API",
    description="API para acesso a datasets",
    version="1.0.0"
)

@app.get("/")#lista as infomrcoes
def root():
    return {
        "status": "API funcionando 🚀",
        "health": "ok",
        "datasets": [
            {
                "id": 1,
                "name": "vendas_2024.csv",
                "source": "google_drive",
                "rows": 12000
            },
            {
                "id": 2,
                "name": "clientes.xlsx",
                "source": "google_drive",
                "rows": 3500
            }
        ]
    }


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/datasets")
def list_datasets():
    return [
        {
            "id": 1,
            "name": "vendas_2024.csv",
            "source": "google_drive",
            "rows": 12000
        },
        {
            "id": 2,
            "name": "clientes.xlsx",
            "source": "google_drive",
            "rows": 3500
        }
    ]
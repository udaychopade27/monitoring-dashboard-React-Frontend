from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.grafana.routes import router as grafana_router

app = FastAPI(title="Grafana Read-Only Proxy")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

app.include_router(grafana_router)

@app.get("/health")
def health():
    return {"status": "ok"}

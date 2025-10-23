from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from prometheus_fastapi_instrumentator import Instrumentator

from .routers import receivables

api = FastAPI(title="Receivables Discount API", version="1.0.0")

# métricas Prometheus
Instrumentator().instrument(api).expose(api, endpoint="/metrics")

# caminhos do front
BASE_DIR = Path(__file__).resolve().parent
INDEX_PATH = BASE_DIR / "web" / "index.html"

# servir arquivos estáticos (favicon, logo, css)
api.mount("/assets", StaticFiles(directory=BASE_DIR / "web" / "assets"), name="assets")

# página inicial (carrega o index.html do app/web)
@api.get("/", response_class=HTMLResponse)
def root():
    return FileResponse(INDEX_PATH)

# healthcheck
@api.get("/health")
def health():
    return {"status": "ok"}

# rotas de negócio
api.include_router(receivables.router, prefix="/receivables", tags=["receivables"])

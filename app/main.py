from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator
from .routers import receivables

api = FastAPI(title="Receivables Discount API", version="1.0.0")

Instrumentator().instrument(api).expose(api, endpoint="/metrics")

@api.get("/health")
def health():
    return {"status": "ok"}

api.include_router(receivables.router, prefix="/receivables", tags=["receivables"])

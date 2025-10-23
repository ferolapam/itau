from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field, field_validator
from typing import Literal
from ..service.receivables import quote_receivable

router = APIRouter()

class QuoteRequest(BaseModel):
    valor_nominal: float = Field(gt=0)
    taxa_mensal: float = Field(ge=0)
    dias_ate_vencimento: int = Field(ge=1, le=365)
    tipo: Literal["DESCONTO", "ANTECIPACAO"] = "DESCONTO"

    @field_validator("taxa_mensal")
    @classmethod
    def taxa_reasonable(cls, v):
        if v > 1:
            raise ValueError("taxa_mensal deve ser fracionária (ex.: 0.03 para 3%)")
        return v

class QuoteResponse(BaseModel):
    valor_nominal: float
    desagio: float
    iof: float
    valor_liquido: float
    taxa_mensal: float
    dias_ate_vencimento: int
    tipo: str

@router.post("/discount/quote", response_model=QuoteResponse)
def discount_quote(body: QuoteRequest):
    try:
        result = quote_receivable(
            valor_nominal=body.valor_nominal,
            taxa_mensal=body.taxa_mensal,
            dias=body.dias_ate_vencimento,
            tipo=body.tipo,
        )
        return QuoteResponse(**result)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

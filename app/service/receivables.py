from math import pow

def _daily_rate_from_monthly(monthly_rate: float) -> float:
    return pow(1 + monthly_rate, 1/30) - 1

def _iof_demo(valor: float, dias: int) -> float:
    iof_rate = min(0.0038 * dias, 0.013)
    return round(valor * iof_rate, 2)

def quote_receivable(valor_nominal: float, taxa_mensal: float, dias: int, tipo: str):
    if valor_nominal <= 0:
        raise ValueError("valor_nominal deve ser > 0")
    if taxa_mensal < 0 or taxa_mensal > 1:
        raise ValueError("taxa_mensal inválida (usar fração, ex.: 0.03)")
    if dias < 1 or dias > 365:
        raise ValueError("dias deve estar entre 1 e 365")
    if tipo not in ("DESCONTO", "ANTECIPACAO"):
        raise ValueError("tipo inválido")

    taxa_dia = _daily_rate_from_monthly(taxa_mensal)
    desagio = round(valor_nominal * taxa_dia * dias, 2)
    iof = _iof_demo(valor_nominal, dias)
    valor_liquido = round(valor_nominal - desagio - iof, 2)

    return {
        "valor_nominal": round(valor_nominal, 2),
        "desagio": desagio,
        "iof": iof,
        "valor_liquido": valor_liquido,
        "taxa_mensal": taxa_mensal,
        "dias_ate_vencimento": dias,
        "tipo": tipo,
    }

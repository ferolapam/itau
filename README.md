# 📡 Itaú — Recebíveis PJ (Backend FastAPI)

<p align="center">
  <img src="app/web/assets/logo.svg" alt="Logo" height="64" />
</p>

**Backend em FastAPI** com UI mínima, testes, observabilidade e CI.  
Simula **desconto/antecipação de recebíveis** para Produtos Ativos PJ (Atacado).

[🧪 Swagger](http://127.0.0.1:8000/docs) · [🖥️ UI](http://127.0.0.1:8000/) · [📈 Métricas](http://127.0.0.1:8000/metrics)

![CI](https://github.com/ferolapam/itau/actions/workflows/ci.yml/badge.svg)

---

## 🔧 Exemplo de requisição (POST `/receivables/discount/quote`)
```json
{
  "valor_nominal": 10000,
  "taxa_mensal": 0.03,
  "dias_ate_vencimento": 30,
  "tipo": "DESCONTO"
}


# Itaú – Engenharia TI Pleno (Backend Java/Python/AWS)

Serviço backend completo com FastAPI, testes, CI/CD, observabilidade e Terraform mínimo (AWS).  
Projeto pronto para execução local no Windows sem necessidade de Docker ou Terraform.

## 🔧 Stack
- Python 3.12 + FastAPI
- Testes: pytest
- Qualidade: black, flake8, isort
- Observabilidade: Prometheus (`/metrics`)
- CI/CD: GitHub Actions
- IaC: Terraform (S3 e DynamoDB demo)

## ▶️ Executar localmente
```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:api --reload
# http://127.0.0.1:8000/docs
```

## ▶️ Testes
```bash
pytest -q
```

## ▶️ Docker (opcional)
```bash
docker build -t receivables-backend:dev .
docker run -p 8000:8000 receivables-backend:dev
```

## ▶️ Terraform (opcional)
```bash
cd terraform
terraform init
terraform plan -var="project_name=receivables-demo" -var="region=sa-east-1"
```

## Endpoints principais
- `POST /receivables/discount/quote` → simulação de desconto/antecipação.
- `GET /health` → status do sistema.
- `GET /metrics` → métricas Prometheus.

## Licença
MIT.

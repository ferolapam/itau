test:
	pytest -q
lint:
	black --check . && isort --check-only . && flake8 .
run:
	uvicorn app.main:api --reload

# pr-aide
High-performance async Python API skeleton with Redis caching, FastAPI, CI, and tests.


## Features
- **FastAPI** service with `/health` and `/fib` (cached) endpoints
- **Async Redis** caching (falls back to in-memory for tests)
- **Quality**: black, isort, mypy, ruff, pytest (CI on GitHub Actions)
- **Containers**: Dockerfile + docker-compose (API + Redis)
- **Bench**: simple async script reporting throughput and p95


## Quickstart
```bash
# 1) Setup
python -m venv .venv && source .venv/bin/activate
pip install -e .[dev]
pre-commit install


# 2) Run API (local)
export CACHE_BACKEND=memory
uvicorn app.main:app --reload
# http://127.0.0.1:8000/docs


# 3) Docker (API + Redis)
docker compose up --build
# API: http://127.0.0.1:8000 | Redis: 6379


# 4) Tests & checks
pytest -q
black --check . && isort --check-only . && mypy . && ruff check .


# 5) Bench (with API running)
python scripts/bench.py

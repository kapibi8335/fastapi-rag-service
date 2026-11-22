# FastAPI RAG Service

Minimal FastAPI service that answers questions through an OpenAI-compatible
chat endpoint.

## Setup

```sh
python3 -m venv .venv && . .venv/bin/activate
pip install -r requirements.txt
set -a; . ./.env; set +a
uvicorn app.main:app --reload
```

## Endpoints

- `GET /health`
- `POST /ask?question=...`

Configuration is read from the environment; see `.env.example`.

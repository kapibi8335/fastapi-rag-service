import os

from fastapi import FastAPI
from openai import OpenAI

app = FastAPI(title="RAG Service")
client = OpenAI(
    base_url=os.environ["OPENAI_BASE_URL"],
    api_key=os.environ["OPENAI_API_KEY"],
)
MODEL = os.environ.get("OPENAI_MODEL", "kimi-k3.1-pro-abliterated")


@app.get("/health")
def health():
    return {"ok": True}


@app.post("/ask")
def ask(question: str):
    r = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": question}],
        max_tokens=256,
    )
    return {"answer": r.choices[0].message.content}

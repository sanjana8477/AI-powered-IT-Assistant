from fastapi import FastAPI, HTTPException
from .models import Ticket, Question
from .db import collection, embedding_model
from .ollama_client import ask_ollama, ollama_healthcheck
import logging

app = FastAPI()
logger = logging.getLogger(__name__)

@app.on_event("startup")
def warmup_ollama():
    # Pre-load the model to avoid first-call latency
    try:
        ask_ollama("Say hello to warm up the model.")
        logger.info("Ollama model warmed up.")
    except Exception as e:
        logger.error(f"Ollama warmup failed: {e}")

@app.post("/recommend-resolution")
async def recommend_resolution(ticket: Ticket):
    try:
        answer = ask_ollama(
            f"Recommend IT fixes for: {ticket.description}. "
            "Provide 3 concise steps in markdown format."
        )
        return {"resolution": answer}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/search-similar-incidents")
async def search_similar(ticket: Ticket):
    query_embedding = embedding_model.encode(ticket.description).tolist()
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=2
    )
    return {
        "similar_tickets": [
            {"description": doc, "resolution": meta["resolution"]}
            for doc, meta in zip(results["documents"][0], results["metadatas"][0])
        ]
    }

@app.post("/ask-assistant")
async def ask_assistant(query: Question):
    try:
        if not ollama_healthcheck():
            raise HTTPException(status_code=503, detail="Ollama service unavailable")
        response = ask_ollama(
            f"Answer concisely: {query.question}. Provide troubleshooting steps if applicable."
        )
        return {"reply": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
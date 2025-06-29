import requests
import logging

logger = logging.getLogger(__name__)

OLLAMA_URL = "http://localhost:11434"

def ask_ollama(prompt: str) -> str:
    try:
        response = requests.post(
            f"{OLLAMA_URL}/api/chat",
            json={
                "model": "phi3:mini",
                "messages": [{"role": "user", "content": prompt}],
                "stream": False
            },
            timeout=120
        )
        response.raise_for_status()
        return response.json()["message"]["content"]
    except Exception as e:
        logger.error(f"Ollama error: {e}")
        raise

def ollama_healthcheck() -> bool:
    try:
        resp = requests.get(OLLAMA_URL, timeout=5)
        return resp.status_code == 200
    except Exception:
        return False
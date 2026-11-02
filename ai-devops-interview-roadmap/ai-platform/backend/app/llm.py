"""LLM adapter placeholder; mock mode works without credentials."""
import os

def provider_name() -> str:
    return os.getenv("LLM_PROVIDER", "mock").lower()

def generate_text(task: str, payload: dict) -> dict:
    """Implement a provider SDK adapter here and validate its structured output."""
    if provider_name() != "mock":
        raise NotImplementedError("Implement your provider adapter before changing LLM_PROVIDER.")
    return {"mode": "mock", "task": task, "payload": payload}

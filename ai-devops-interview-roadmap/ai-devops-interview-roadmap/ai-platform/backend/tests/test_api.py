from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

def test_question():
    response = client.post("/api/interview/question", json={
        "topic": "Kubernetes", "level": "intermediate",
        "question_type": "scenario", "target_role": "DevOps Engineer"
    })
    assert response.status_code == 200
    assert "question" in response.json()

def test_evaluate():
    response = client.post("/api/interview/evaluate", json={
        "question": "How do you debug a Pod?",
        "answer": "Inspect events and logs, check probes and config, validate the fix and monitor rollout.",
        "topic": "Kubernetes", "level": "intermediate"
    })
    assert response.status_code == 200
    assert 1 <= response.json()["score"] <= 5

from fastapi import FastAPI
from .schemas import InterviewStart, AnswerSubmission
from .agents import planner_agent, question_agent, evaluator_agent

app = FastAPI(title="AI DevOps Interview Coach", version="0.1.0",
              description="Starter API for roadmap planning, interview questions and feedback.")

@app.get("/health")
def health():
    return {"status": "ok", "mode": "starter"}

@app.post("/api/roadmap")
def create_roadmap(profile: dict):
    return planner_agent(profile)

@app.post("/api/interview/question")
def create_question(request: InterviewStart):
    return question_agent(request)

@app.post("/api/interview/evaluate")
def evaluate_answer(request: AnswerSubmission):
    return evaluator_agent(request)

from .schemas import InterviewStart, AnswerSubmission, Evaluation
from .llm import generate_text

def planner_agent(profile: dict) -> dict:
    generate_text("plan_learning_path", profile)
    return {"milestones": [
        {"topic": "Linux and networking", "task": "Diagnose a service and trace a request"},
        {"topic": "Docker and Kubernetes", "task": "Deploy and troubleshoot a sample app"},
        {"topic": "AWS and Terraform", "task": "Design a sandbox platform"},
        {"topic": "CI/CD and observability", "task": "Build a pipeline and dashboard"}
    ], "note": "Starter plan; personalize after a skills assessment."}

def question_agent(request: InterviewStart) -> dict:
    generate_text("generate_question", request.model_dump())
    return {
        "question": f"[Mock] Explain a real-world {request.topic} problem for a {request.level} {request.target_role}. How would you investigate and resolve it?",
        "expected_signals": ["Clarifies impact", "Uses evidence and structured debugging", "Explains safe mitigation", "Validates and prevents recurrence"],
        "follow_up": "What signals would you monitor to confirm resolution?"
    }

def evaluator_agent(submission: AnswerSubmission) -> Evaluation:
    generate_text("evaluate_answer", submission.model_dump())
    if len(submission.answer.strip()) < 30:
        score, strengths = 1, ["You attempted the question"]
        gaps = ["Explain the process step by step", "Include commands or evidence", "Discuss validation and prevention"]
    else:
        score, strengths = 3, ["You provided a substantive response"]
        gaps = ["Add specific commands and observable evidence", "Discuss rollback, validation and prevention"]
    return Evaluation(score=score, strengths=strengths, gaps=gaps,
        improved_answer="Establish impact and scope; gather events, logs, metrics and recent changes; form and test hypotheses; apply the safest mitigation; verify recovery; document prevention. Add technology-specific commands and explain why each step matters.",
        follow_up="Which command or metric would you check first, and what would its result tell you?")

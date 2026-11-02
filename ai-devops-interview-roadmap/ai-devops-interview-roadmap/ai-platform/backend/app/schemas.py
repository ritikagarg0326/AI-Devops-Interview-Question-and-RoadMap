from pydantic import BaseModel, Field
from typing import Literal

Level = Literal["beginner", "intermediate", "advanced"]
QuestionType = Literal["concept", "hands_on", "scenario", "architecture"]

class InterviewStart(BaseModel):
    topic: str = Field(min_length=2, max_length=80)
    level: Level = "intermediate"
    question_type: QuestionType = "scenario"
    target_role: str = "DevOps Engineer"

class AnswerSubmission(BaseModel):
    question: str = Field(min_length=5, max_length=3000)
    answer: str = Field(min_length=1, max_length=10000)
    topic: str = "DevOps"
    level: Level = "intermediate"

class Evaluation(BaseModel):
    score: int = Field(ge=1, le=5)
    strengths: list[str]
    gaps: list[str]
    improved_answer: str
    follow_up: str
    disclaimer: str = "Mock evaluation. Verify technical details and use this as practice feedback."

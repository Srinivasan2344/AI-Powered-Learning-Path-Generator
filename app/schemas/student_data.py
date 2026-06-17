from pydantic import BaseModel


class StudentCreate(BaseModel):
    student_id: int
    goal: str
    available_hours_per_week: int
    completed_topics: list[str]
    assessment_scores: dict
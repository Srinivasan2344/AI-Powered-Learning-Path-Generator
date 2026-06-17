from pydantic import BaseModel
from typing import Dict, List


class StudentProfile(BaseModel):
    student_id: int
    goal: str
    completed_topics: List[str]
    assessment_scores: Dict[str, int]
    available_hours_per_week: int
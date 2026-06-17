from pydantic import BaseModel


class EngagementInput(BaseModel):
    student_id: int
    login_frequency: int
    assignment_completion_rate: float
    quiz_attempts: int
    study_hours_per_week: int
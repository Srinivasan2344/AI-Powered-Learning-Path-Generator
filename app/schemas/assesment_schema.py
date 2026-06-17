from pydantic import BaseModel

class AssessmentCreate(BaseModel):
    student_id: int
    topic: str
    score: int
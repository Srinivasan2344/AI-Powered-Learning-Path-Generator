from fastapi import APIRouter
from app.schemas.learning_path_schema import StudentProfile
from app.services.learning_path_service import (
    generate_learning_path,
    generate_study_schedule
)

router = APIRouter()


@router.post("/generate-learning-path")
def create_learning_path(student: StudentProfile):
    path = generate_learning_path(student)

    schedule = generate_study_schedule(
        path,
        student.available_hours_per_week
    )

    return {
        "student_id": student.student_id,
        "goal": student.goal,
        "learning_path": path,
        "study_schedule": schedule
    }
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.database.models import Student
from app.schemas.student_data import StudentCreate

router = APIRouter()


@router.post("/students")
def create_student(student: StudentCreate,
                   db: Session = Depends(get_db)):

    db_student = Student(
        student_id=student.student_id,
        goal=student.goal,
        available_hours_per_week=student.available_hours_per_week
    )

    db.add(db_student)
    db.commit()
    db.refresh(db_student)

    return {
        "message": "Student created successfully",
        "id": db_student.id
    }
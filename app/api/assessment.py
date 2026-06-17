from fastapi import APIRouter, Depends  # type: ignore[import]
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.database.models import Assessment
from app.schemas.assesment_schema import AssessmentCreate

router = APIRouter()


@router.post("/assessments")
def create_assessment(
    assessment: AssessmentCreate,
    db: Session = Depends(get_db)
):

    db_assessment = Assessment(
        student_id=assessment.student_id,
        topic=assessment.topic,
        score=assessment.score
    )

    db.add(db_assessment)
    db.commit()
    db.refresh(db_assessment)

    return {
        "message": "Assessment saved successfully",
        "assessment_id": db_assessment.id
    }
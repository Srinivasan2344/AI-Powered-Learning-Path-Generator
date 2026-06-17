from fastapi import APIRouter
from app.schemas.learning_path_schema import StudentProfile
from app.services.knowledge_gap_services import detect_knowledge_gaps

router = APIRouter()


@router.post("/knowledge-gaps")
def analyze_knowledge_gaps(student: StudentProfile):
    weak_topics = detect_knowledge_gaps(
        student.assessment_scores
    )

    return {
        "student_id": student.student_id,
        "weak_topics": weak_topics,
        "revision_recommendations": [
            f"Revise {topic}" for topic in weak_topics
        ]
    }
from fastapi import APIRouter
from app.schemas.learning_path_schema import StudentProfile
from app.services.knowledge_gap_services import detect_knowledge_gaps
from app.services.quiz_recommendation_services import recommend_quizzes

router = APIRouter()


@router.post("/quiz-recommendations")
def get_quiz_recommendations(student: StudentProfile):

    weak_topics = detect_knowledge_gaps(
        student.assessment_scores
    )

    quizzes = recommend_quizzes(weak_topics)

    return {
        "student_id": student.student_id,
        "weak_topics": weak_topics,
        "recommended_quizzes": quizzes
    }
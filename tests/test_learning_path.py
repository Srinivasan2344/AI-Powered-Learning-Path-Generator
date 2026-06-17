from app.schemas.student_data import StudentCreate
from app.services.learning_path_service import generate_learning_path


def test_learning_path():

    student = StudentCreate(
        student_id=101,
        goal="Machine Learning",
        available_hours_per_week=10,
        completed_topics=["Python"],
        assessment_scores={"Python": 90}
    )

    result = generate_learning_path(student)

    assert result is not None
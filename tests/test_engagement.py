from app.schemas.engagement_schemas import EngagementInput
from app.services.engagement_service import predict_engagement_risk

def test_engagement():
    student = EngagementInput(
        student_id=101,
        login_frequency=1,
        assignment_completion_rate=20,
        quiz_attempts=1,
        study_hours_per_week=1
    )

    result = predict_engagement_risk(student)

    assert "risk_level" in result
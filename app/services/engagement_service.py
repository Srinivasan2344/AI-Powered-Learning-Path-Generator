from app.schemas.engagement_schemas import EngagementInput


def predict_engagement_risk(student: EngagementInput):

    score = 0

    # Login frequency analysis
    if student.login_frequency < 2:
        score += 30
    elif student.login_frequency < 5:
        score += 15

    # Assignment completion analysis
    if student.assignment_completion_rate < 50:
        score += 30
    elif student.assignment_completion_rate < 75:
        score += 15

    # Quiz participation analysis
    if student.quiz_attempts < 2:
        score += 20
    elif student.quiz_attempts < 5:
        score += 10

    # Study hours analysis
    if student.study_hours_per_week < 3:
        score += 20
    elif student.study_hours_per_week < 6:
        score += 10

    # Risk level classification
    if score >= 70:
        risk_level = "High"
    elif score >= 40:
        risk_level = "Medium"
    else:
        risk_level = "Low"

    return {
        "student_id": student.student_id,
        "risk_score": score,
        "risk_level": risk_level
    }
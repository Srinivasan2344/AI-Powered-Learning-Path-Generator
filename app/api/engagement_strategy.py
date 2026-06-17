from typing import Dict, Any
from fastapi import APIRouter
from app.schemas.engagement_schemas import EngagementInput
from app.services.engagement_service import predict_engagement_risk
from app.services.engagement_strategy_service import (
    generate_engagement_strategy
)

router = APIRouter()


@router.post("/engagement-strategy")
def get_strategy(student: EngagementInput):

    result = predict_engagement_risk(student)

    return {
        "student_id": student.student_id,
        "risk_level": result["risk_level"],
        "engagement_strategies":
            generate_engagement_strategy(
                result["risk_level"]
            )
    }
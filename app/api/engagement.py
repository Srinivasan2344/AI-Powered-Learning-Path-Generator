from fastapi import APIRouter
from app.schemas.engagement_schemas import EngagementInput
from app.services.engagement_service import predict_engagement_risk 

router=APIRouter()

@router.post("/engagement-prediction")
def predict_engagement(student: EngagementInput):
    result=predict_engagement_risk(student)

    return{
        "student_id":student.student_id,
        ** result
    }
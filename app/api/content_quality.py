from fastapi import APIRouter

from app.schemas.quality_schemas import QualityInput
from app.services.content_quality_service import evaluate_content

router = APIRouter()


@router.post("/evaluate-content")
def evaluate(request: QualityInput):

    return evaluate_content(request.content)
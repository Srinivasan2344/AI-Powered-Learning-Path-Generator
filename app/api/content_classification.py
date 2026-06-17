from fastapi import APIRouter
from app.schemas.content_schema import ContentInput
from app.services.content_classification_service import classify_content

router = APIRouter()


@router.post("/classify-content")
def classify(request: ContentInput):

    return classify_content(request.content)
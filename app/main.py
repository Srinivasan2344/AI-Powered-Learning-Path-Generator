from fastapi import FastAPI
from .api.learning_path import router as learning_path_router
from .database.connection import engine
from .database.models import Base
from .api.student_api import router as student_router
from app.api.knowledge_api import router as knowledge_gap_router
from app.api.quiz_recommendation_api import (router as quiz_router)
from app.api.engagement import router as engagement_router
from app.api.assessment import router as assessment_router
from app.api.monitoring import (router as monitoring_router)
from app.api.content_classification import (router as content_router)
from app.api.content_quality import (router as quality_router)
Base.metadata.create_all(bind=engine)

app = FastAPI(title="AI Learning Platform",version="1.0.0")

app.include_router(learning_path_router)
app.include_router(student_router)
app.include_router(knowledge_gap_router)
app.include_router(quiz_router)
app.include_router(engagement_router)
app.include_router(assessment_router)
app.include_router(monitoring_router)
app.include_router(content_router)
app.include_router(quality_router)

@app.get("/")
def root():
    return {"message": "AI Learning Platform API is running!"}
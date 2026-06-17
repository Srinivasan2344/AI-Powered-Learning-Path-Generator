from fastapi import APIRouter
from app.services.monitoring_service import get_system_metrics

router = APIRouter()

@router.get("/monitoring/metrics")
def metrics():
    return get_system_metrics()
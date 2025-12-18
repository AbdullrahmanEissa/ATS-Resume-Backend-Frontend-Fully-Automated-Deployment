from fastapi import APIRouter
from models.schemas import HealthResponse

router = APIRouter()

@router.get("/health", response_model=HealthResponse)
async def health_check():
    return HealthResponse(
        status="healthy",
        message="ATS CV Scanner API is running"
    )
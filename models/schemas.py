from pydantic import BaseModel, Field
from typing import List, Optional

class HealthResponse(BaseModel):
    status: str
    message: str

class UploadResponse(BaseModel):
    file_id: str
    filename: str
    message: str

class AnalyzeRequest(BaseModel):
    file_id: str
    job_description: str

class AnalyzeResponse(BaseModel):
    file_id: str
    filename: str
    score: float
    matched_keywords: List[str]
    total_keywords: int
    extracted_text_preview: str
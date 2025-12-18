from fastapi import APIRouter, HTTPException
from pathlib import Path
import config
from models.schemas import AnalyzeRequest, AnalyzeResponse
from services.cv_parser import CVParser
from services.scorer import ATSScorer

router = APIRouter()

@router.post("/analyze", response_model=AnalyzeResponse)
async def analyze_cv(request: AnalyzeRequest):
    if not request.job_description.strip():
        raise HTTPException(status_code=400, detail="Job description cannot be empty")
    
    matching_files = list(config.UPLOAD_DIR.glob(f"{request.file_id}.*"))
    
    if not matching_files:
        raise HTTPException(status_code=404, detail="File not found")
    
    file_path = matching_files[0]
    
    try:
        cv_text = CVParser.parse_cv(file_path)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to parse CV: {str(e)}")
    
    if not cv_text.strip():
        raise HTTPException(status_code=400, detail="CV appears to be empty")
    
    score, matched_keywords, total_keywords = ATSScorer.score_cv(cv_text, request.job_description)
    
    preview_length = 200
    text_preview = cv_text[:preview_length] + "..." if len(cv_text) > preview_length else cv_text
    
    return AnalyzeResponse(
        file_id=request.file_id,
        filename=file_path.name,
        score=score,
        matched_keywords=matched_keywords,
        total_keywords=total_keywords,
        extracted_text_preview=text_preview
    )
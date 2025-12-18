from fastapi import APIRouter, UploadFile, File, HTTPException
from pathlib import Path
import uuid
import config
from models.schemas import UploadResponse

router = APIRouter()

@router.post("/upload-cv", response_model=UploadResponse)
async def upload_cv(file: UploadFile = File(...)):
    if not file.filename:
        raise HTTPException(status_code=400, detail="No file provided")
    
    file_extension = Path(file.filename).suffix.lower()
    if file_extension not in config.ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid file type. Allowed: {', '.join(config.ALLOWED_EXTENSIONS)}"
        )
    
    content = await file.read()
    if len(content) > config.MAX_FILE_SIZE:
        raise HTTPException(status_code=400, detail="File too large. Max size: 10MB")
    
    file_id = str(uuid.uuid4())
    file_path = config.UPLOAD_DIR / f"{file_id}{file_extension}"
    
    try:
        with open(file_path, "wb") as f:
            f.write(content)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to save file: {str(e)}")
    
    return UploadResponse(
        file_id=file_id,
        filename=file.filename,
        message="File uploaded successfully"
    )
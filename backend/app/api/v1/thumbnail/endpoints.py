from fastapi import APIRouter, UploadFile, File, HTTPException, Depends
from sqlalchemy.orm import Session
from app.core.configs.database import db
from app.core.schemas.thumbnail import ThumbnailCreate, ThumbnailResponse
from app.services.image_analyser import analyze_thumbnail
from app.db.crud.thumbnail import create_thumbnail_record
from io import BytesIO
from PIL import Image

router = APIRouter()


@router.post("/", response_model=ThumbnailResponse)
async def upload_thumbnail(
    file: UploadFile = File(...), db_session: Session = Depends(db.get_db)
):
    """
    Upload a thumbnail image, analyze it, and get feedback (score and suggestions).
    """
    image_bytes = await file.read()

    try:
        Image.open(BytesIO(image_bytes))
    except Exception:
        raise HTTPException(status_code=400, detail="Format d'image invalide")

    analysis_result = await analyze_thumbnail(image_bytes)
    thumbnail_data = ThumbnailCreate(
        image_url=file.filename,
        score=analysis_result.get("score", 5),
        comment=analysis_result.get("comment", "Analyse réussie de la miniature !"),
    )

    created_thumbnail = create_thumbnail_record(db_session, thumbnail_data)

    return ThumbnailResponse(
        id=created_thumbnail.id,
        image_url=created_thumbnail.image_url,
        score=created_thumbnail.score,
        comment=created_thumbnail.comment,
        created_at=created_thumbnail.created_at.strftime("%Y-%m-%d %H:%M:%S"),
    )

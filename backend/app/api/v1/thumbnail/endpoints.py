from fastapi import APIRouter, UploadFile, File, Depends
from sqlalchemy.orm import Session
from io import BytesIO
from PIL import Image
import imghdr

from app.core.handlers.error import ErrorHandler
from app.core.configs.database import db
from app.core.schemas.thumbnail import ThumbnailCreate, ThumbnailResponse
from app.services.image_analyser import analyze_thumbnail
from app.db.crud.thumbnail import create_thumbnail_record

# --- Variables
router = APIRouter()
ALLOWED_IMAGE_TYPES = {"jpeg", "png"}


@router.post("/", response_model=ThumbnailResponse)
async def upload_thumbnail(
    file: UploadFile = File(...), db_session: Session = Depends(db.get_db)
):
    """
    Uploads a YouTube thumbnail image, analyzes it using the Groq API, and returns a score and suggestions for improvement.

    This endpoint processes an uploaded image file, ensures that the file is a valid image type,
    and then sends the image for analysis. The analysis generates a score (1-10) and a comment, which
    are saved in the database along with the image URL.

    Parameters:
    file (UploadFile): The uploaded image file to be processed.
    db_session (Session): The database session used for saving the thumbnail analysis result.

    Returns:
    ThumbnailResponse: A JSON response containing the thumbnail's ID, image URL, score, comment,
    and the timestamp of when the thumbnail record was created.

    Raises:
    HTTPException: Raised if the file is not a valid image type, if the image is corrupted, or if there
    is an error during the analysis process.
    """
    image_bytes = await file.read()

    if not imghdr.what(None, h=image_bytes) in ALLOWED_IMAGE_TYPES:
        ErrorHandler.handle_invalid_file_type()

    try:
        Image.open(BytesIO(image_bytes))
    except Exception:
        ErrorHandler.handle_invalid_image()

    try:
        analysis_result = await analyze_thumbnail(image_bytes)
    except Exception as e:
        ErrorHandler.handle_groq_error(str(e))

    thumbnail_data = ThumbnailCreate(
        image_url=file.filename,
        score=analysis_result.get("score", 5),
        comment=analysis_result.get("comment", "Successful thumbnail analysis!"),
    )

    created_thumbnail = create_thumbnail_record(db_session, thumbnail_data)

    return ThumbnailResponse(
        id=created_thumbnail.id,
        image_url=created_thumbnail.image_url,
        score=created_thumbnail.score,
        comment=created_thumbnail.comment,
        created_at=created_thumbnail.created_at.strftime("%Y-%m-%d %H:%M:%S"),
    )

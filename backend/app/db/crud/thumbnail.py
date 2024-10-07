from sqlalchemy.orm import Session
from app.db.models.thumbnail import Thumbnail
from app.core.schemas.thumbnail import ThumbnailCreate
from datetime import datetime


def create_thumbnail_record(db: Session, thumbnail: ThumbnailCreate):
    """
    Save the thumbnail information into the database.

    This function creates a new record in the 'thumbnails' table based on the provided
    ThumbnailCreate schema and commits it to the database.

    Parameters:
    db (Session): The SQLAlchemy database session used to interact with the database.
    thumbnail (ThumbnailCreate): A Pydantic schema containing the data for the thumbnail,
    including image URL, score, and comment.

    Returns:
    Thumbnail: The saved Thumbnail object from the database with an assigned ID and timestamp.
    """
    db_thumbnail = Thumbnail(
        image_url=thumbnail.image_url,
        score=thumbnail.score,
        comment=thumbnail.comment,
        created_at=datetime.now(),
    )
    db.add(db_thumbnail)
    db.commit()
    db.refresh(db_thumbnail)
    return db_thumbnail

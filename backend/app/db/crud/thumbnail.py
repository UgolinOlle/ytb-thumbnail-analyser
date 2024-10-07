from sqlalchemy.orm import Session
from app.db.models.thumbnail import Thumbnail
from app.core.schemas.thumbnail import ThumbnailCreate
from datetime import datetime


def create_thumbnail_record(db: Session, thumbnail: ThumbnailCreate):
    """
    Sauvegarder les informations d'une miniature dans la base de données.
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

from sqlalchemy import Column, Integer, Text, TIMESTAMP
from sqlalchemy.dialects.mysql import TINYINT
from sqlalchemy.sql import func
from app.core.configs.database import db


class Thumbnail(db.Base):
    __tablename__ = "thumbnails"
    __table_args__ = {"mysql_collate": "utf8mb4_unicode_ci"}

    id = Column(Integer, primary_key=True, index=True)
    image_url = Column(Text(collation="utf8mb4_unicode_ci"), nullable=False)
    score = Column(TINYINT, nullable=False)
    comment = Column(Text(collation="utf8mb4_unicode_ci"), nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)

from sqlalchemy import Column, Integer, Text, TIMESTAMP
from sqlalchemy.dialects.mysql import TINYINT
from sqlalchemy.sql import func
from app.core.configs.database import db


class Thumbnail(db.Base):
    """
    Represents the 'thumbnails' table in the database, which stores information
    about uploaded YouTube thumbnails, their analysis score, and the comment generated.

    Attributes:
    __tablename__ (str): The name of the table in the database ('thumbnails').
    __table_args__ (dict): Additional table arguments, here specifying MySQL collation.
    id (int): Primary key of the table, auto-incremented.
    image_url (str): URL of the uploaded image (collation: utf8mb4_unicode_ci).
    score (int): Score between 1 and 10, representing the quality of the thumbnail.
    comment (str): Feedback or suggestions for improving the thumbnail (collation: utf8mb4_unicode_ci).
    created_at (TIMESTAMP): The timestamp when the thumbnail record was created.
    """

    __tablename__ = "thumbnails"
    __table_args__ = {"mysql_collate": "utf8mb4_unicode_ci"}

    id = Column(Integer, primary_key=True, index=True)
    image_url = Column(Text(collation="utf8mb4_unicode_ci"), nullable=False)
    score = Column(TINYINT, nullable=False)
    comment = Column(Text(collation="utf8mb4_unicode_ci"), nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)

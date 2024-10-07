from pydantic import BaseModel


class ThumbnailCreate(BaseModel):
    """
    Represents the data required to create a new thumbnail record.

    Attributes:
    image_url (str): The URL of the uploaded thumbnail image.
    score (int): The score between 1 and 10 that evaluates the quality of the thumbnail.
    comment (str): A comment providing feedback on the thumbnail and suggesting improvements.
    """

    image_url: str
    score: int
    comment: str

    class Config:
        from_attributes = True


class ThumbnailResponse(BaseModel):
    """
    Represents the response model for a saved thumbnail, including the
    ID and timestamp of when it was created.

    Attributes:
    id (int): The unique identifier for the thumbnail record.
    image_url (str): The URL of the saved thumbnail image.
    score (int): The score assigned to the thumbnail.
    comment (str): The feedback comment for the thumbnail.
    created_at (str): The timestamp of when the thumbnail record was created.
    """

    id: int
    image_url: str
    score: int
    comment: str
    created_at: str

    class Config:
        from_attributes = True

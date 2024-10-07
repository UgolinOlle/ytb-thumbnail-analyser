from pydantic import BaseModel


class ThumbnailCreate(BaseModel):
    image_url: str
    score: int
    comment: str

    class Config:
        from_attributes = True


class ThumbnailResponse(BaseModel):
    id: int
    image_url: str
    score: int
    comment: str
    created_at: str

    class Config:
        from_attributes = True

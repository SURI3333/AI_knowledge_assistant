from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class DocumentBase(BaseModel):
    filename: str


class DocumentCreate(DocumentBase):
    pass


class DocumentResponse(DocumentBase):
    id: int
    user_id: Optional[int] = None
    uploaded_at: Optional[datetime] = None

    class Config:
        orm_mode = True
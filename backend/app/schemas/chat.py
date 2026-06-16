from pydantic import BaseModel
from datetime import datetime
from typing import Optional


# ✅ Request Schema (User asks question)
class ChatRequest(BaseModel):
    question: str


# ✅ Response Schema (AI answer)
class ChatResponse(BaseModel):
    answer: str


# ✅ DB / Full Chat History Schema
class ChatHistory(BaseModel):
    id: int
    question: str
    answer: str
    user_id: Optional[int] = None
    created_at: Optional[datetime] = None

    class Config:
        orm_mode = True
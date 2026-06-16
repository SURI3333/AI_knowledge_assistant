from sqlalchemy import Column, Integer, Text, ForeignKey
from app.database import Base

class Chat(Base):
    __tablename__ = "chat"

    id = Column(Integer, primary_key=True)
    question = Column(Text)
    answer = Column(Text)
    user_id = Column(Integer, ForeignKey("users.id"))
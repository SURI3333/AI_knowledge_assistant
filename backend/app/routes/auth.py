from fastapi import APIRouter
from passlib.hash import bcrypt
from app.schemas.user import UserCreate

router = APIRouter()

fake_users = {}

@router.post("/register")
def register(user: UserCreate):
    fake_users[user.email] = bcrypt.hash(user.password[:72])
    return {"msg": "Registered successfully"}


@router.post("/login")
def login(user: UserCreate):
    if user.email not in fake_users:
        return {"error": "Invalid user"}

    if not bcrypt.verify(user.password, fake_users[user.email]):
        return {"error": "Wrong password"}

    return {"msg": "Login success"}
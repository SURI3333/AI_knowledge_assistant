from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def analytics():
    return {
        "documents": 5,
        "questions": 10
    }
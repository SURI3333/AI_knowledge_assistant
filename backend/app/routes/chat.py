from fastapi import APIRouter
from app.schemas.chat import ChatRequest
from app.services.vector_service import search_chunks
from app.services.ai_service import get_answer

router = APIRouter()

@router.post("/ask")
def ask_question(data: ChatRequest):

    try:
        question = data.question
        print("Question:", question)   # ✅ debug

        docs = search_chunks(question)

        print("Docs Found:", docs)     # ✅ debug

        # ✅ Fix: handle empty vector DB
        if not docs or len(docs) == 0:
            return {"answer": "⚠️ Please upload document first."}

        context = "\n".join([doc.page_content for doc in docs])

        print("Context:", context[:200])   # ✅ debug preview

        answer = get_answer(context, question)

        print("Answer:", answer)

        return {"answer": answer}

    except Exception as e:
        print("ERROR IN CHAT:", str(e))   # ✅ IMPORTANT
        return {"answer": f"❌ Error: {str(e)}"}
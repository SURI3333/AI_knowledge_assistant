from fastapi import APIRouter, UploadFile, File
import os
import uuid

# ✅ Import your utilities
from app.utils.file_loader import load_pdf, load_docx, load_txt
from app.utils.chunking import chunk_text
from app.services.vector_service import store_chunks

router = APIRouter()

# ✅ Create uploads folder automatically
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    """
    Upload and process document (PDF, DOCX, TXT)
    """

    try:
        # ✅ Generate unique filename
        file_id = str(uuid.uuid4())

        # ✅ FIX: lowercase extension
        file_ext = file.filename.split(".")[-1].lower()

        file_path = os.path.join(UPLOAD_DIR, f"{file_id}.{file_ext}")

        # ✅ Save file
        with open(file_path, "wb") as f:
            content = await file.read()
            f.write(content)

        # ✅ FIXED: correct file detection
        if file_ext == "pdf":
            text = load_pdf(file_path)

        elif file_ext == "docx":
            text = load_docx(file_path)

        elif file_ext == "txt":
            text = load_txt(file_path)

        else:
            return {"error": "Unsupported file format (use PDF, DOCX, TXT)"}

        # ✅ Check empty content
        if not text or text.strip() == "":
            return {"error": "No readable content found in file"}

        # ✅ Chunk text
        chunks = chunk_text(text)

        # ✅ Store in vector DB
        store_chunks(chunks)

        # ✅ Response
        return {
            "message": "✅ Document uploaded and processed successfully",
            "filename": file.filename,
            "file_type": file_ext,
            "chunks_created": len(chunks)
        }

    except Exception as e:
        return {
            "error": f"❌ Failed to process file: {str(e)}"
        }
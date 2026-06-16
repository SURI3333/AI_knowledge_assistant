import os
import uuid
from app.utils.file_loader import load_pdf, load_docx, load_txt
from app.utils.chunking import chunk_text
from app.services.vector_service import store_chunks


UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


def process_document(file):
    """
    Handles document upload, extraction, chunking and vector storage
    """

    # ✅ Generate unique file name
    file_id = str(uuid.uuid4())
    file_ext = file.filename.split(".")[-1].lower()

    file_path = os.path.join(UPLOAD_DIR, f"{file_id}.{file_ext}")

    # ✅ Save file
    with open(file_path, "wb") as f:
        content = file.file.read()
        f.write(content)

    # ✅ Extract text
    if file_ext == "pdf":
        text = load_pdf(file_path)

    elif file_ext == "docx":
        text = load_docx(file_path)

    elif file_ext == "txt":
        text = load_txt(file_path)

    else:
        raise Exception("Unsupported file format")

    # ✅ Validate text
    if not text or text.strip() == "":
        raise Exception("No readable content found")

    # ✅ Chunk text
    chunks = chunk_text(text)

    # ✅ Store in vector DB
    store_chunks(chunks)

    return {
        "filename": file.filename,
        "chunks": len(chunks)
    }
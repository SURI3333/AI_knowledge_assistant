from pypdf import PdfReader
import docx

def load_pdf(path):
    reader = PdfReader(path)
    text = ""

    for page in reader.pages:
        text += page.extract_text() or ""

    return text


def load_docx(path):
    doc = docx.Document(path)
    return "\n".join([p.text for p in doc.paragraphs])


def load_txt(path):
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        return f.read()
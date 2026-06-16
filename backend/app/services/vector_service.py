from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import Chroma

embedding = OllamaEmbeddings(
    model="nomic-embed-text",
    base_url="http://localhost:11434"
)

db = None

def store_chunks(chunks):
    global db
    db = Chroma.from_texts(chunks, embedding=embedding)

def search_chunks(query):
    try:
        if db is None:
            return []
        return db.similarity_search(query, k=3)
    except Exception as e:
        print("VECTOR ERROR:", e)
        return []
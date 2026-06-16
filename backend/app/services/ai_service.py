from langchain_ollama import ChatOllama

# ✅ Initialize model safely
llm = ChatOllama(
    model="llama2",
    base_url="http://localhost:11434"
)

def get_answer(context, question):
    try:
        prompt = f"""
        Answer only from context.

        Context:
        {context}

        Question:
        {question}
        """

        response = llm.invoke(prompt)

        return response.content

    except Exception as e:
        print("AI ERROR:", e)
        return "❌ AI error occurred"
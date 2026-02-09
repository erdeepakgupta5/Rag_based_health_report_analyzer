import ollama
import numpy as np
from sentence_transformers import SentenceTransformer

embed_model = SentenceTransformer("all-MiniLM-L6-v2")

def ask_question(question, index, chunks):
    q_emb = embed_model.encode([question])
    _, I = index.search(np.array(q_emb), 3)

    context = "\n".join([chunks[i] for i in I[0]])

    prompt = f"""
You are a health report assistant.
Answer ONLY from the provided document.
If not found, say "Information not present in the report".

Document:
{context}

Question:
{question}
"""

    response = ollama.chat(
        model="llama3",
        messages=[{"role": "user", "content": prompt}]
    )

    return response["message"]["content"]

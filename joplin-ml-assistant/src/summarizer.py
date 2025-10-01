# src/summarizer.py

# Use relative imports for package-safe execution
from src import embeddings, llm_interface


def answer_query(query: str) -> str:
    """
    Answer a user query by searching embeddings and running the LLM.
    """
    # Search top 5 relevant chunks
    chunks = embeddings.search(query, k=5)
    context = "\n\n".join(chunks)

    # Prepare prompt for the LLM
    prompt = f"""
You are an assistant that summarizes notes.

Context:
{context}

Question: {query}

Answer clearly and concisely:
"""
    # Run LLM and return answer
    return llm_interface.run_llm(prompt)

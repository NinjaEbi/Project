# src/retrieval.py
from src import embeddings

def retrieve_notes(query: str, top_k: int = 5):
    """
    Retrieve top_k relevant note chunks for a given query.
    """
    results = embeddings.search(query, k=top_k)
    return results

# Example usage for testing
if __name__ == "__main__":
    query = "machine learning"
    notes = retrieve_notes(query, top_k=3)
    print("Top 3 relevant note chunks:\n")
    for i, n in enumerate(notes, 1):
        print(f"{i}. {n}\n{'-'*50}")

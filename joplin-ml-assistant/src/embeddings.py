# src/embeddings.py
import os
import faiss
import numpy as np
import pickle
from sentence_transformers import SentenceTransformer
from src import config

# Load sentence transformer model
model = SentenceTransformer("all-MiniLM-L6-v2")
EMBED_DIM = 384  # MiniLM output dimension

# Ensure embeddings folder exists
os.makedirs(config.EMBEDDINGS_DIR, exist_ok=True)

def build_faiss_index():
    index = faiss.IndexFlatL2(EMBED_DIM)
    texts = []
    vectors = []

    if not os.path.exists(config.PROCESSED_DIR):
        print(f"Processed folder not found: {config.PROCESSED_DIR}")
        return

    files = [f for f in os.listdir(config.PROCESSED_DIR) if f.endswith("_chunks.txt")]
    if not files:
        print(f"No processed chunk files found in {config.PROCESSED_DIR}")
        return

    for fname in files:
        file_path = os.path.join(config.PROCESSED_DIR, fname)
        with open(file_path, "r", encoding="utf-8") as f:
            chunks = f.read().split("\n\n")
            for c in chunks:
                c = c.strip()
                if c:
                    vec = model.encode([c])[0].astype("float32")
                    texts.append(c)
                    vectors.append(vec)

    if not vectors:
        print("No vectors created. Make sure processed files have text.")
        return

    vectors = np.array(vectors).astype("float32")
    index.add(vectors)

    # Save FAISS index
    faiss.write_index(index, os.path.join(config.EMBEDDINGS_DIR, "notes.index"))

    # Save texts as pickle
    with open(os.path.join(config.EMBEDDINGS_DIR, "notes.pkl"), "wb") as f:
        pickle.dump(texts, f)

    print("FAISS index built with", len(texts), "chunks.")

def load_index():
    index_path = os.path.join(config.EMBEDDINGS_DIR, "notes.index")
    texts_path = os.path.join(config.EMBEDDINGS_DIR, "notes.pkl")

    if not os.path.exists(index_path) or not os.path.exists(texts_path):
        print("Embeddings not found. Run build_faiss_index() first.")
        return None, None

    index = faiss.read_index(index_path)
    with open(texts_path, "rb") as f:
        texts = pickle.load(f)

    return index, texts

def search(query, k=5):
    index, texts = load_index()
    if index is None or texts is None:
        return []

    vec = model.encode([query]).astype("float32")
    D, I = index.search(vec, k)
    return [texts[i] for i in I[0]]

# Run script directly
if __name__ == "__main__":
    build_faiss_index()

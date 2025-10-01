# src/preprocess.py
import os
import re
from src import config
from src import joplin_api

def clean_markdown(text: str) -> str:
    """Basic cleaning of markdown (remove links, images, headers, etc.)"""
    text = re.sub(r"!\[.*?\]\(.*?\)", "", text)  # remove images
    text = re.sub(r"\[.*?\]\(.*?\)", "", text)   # remove links
    text = text.replace("#", "").strip()         # remove headers
    return text

def chunk_text(text: str, chunk_size=config.CHUNK_SIZE, overlap=config.CHUNK_OVERLAP):
    """Split text into overlapping chunks"""
    chunks = []
    start = 0
    while start < len(text):
        end = min(start + chunk_size, len(text))
        chunks.append(text[start:end])
        start += chunk_size - overlap
    return chunks

def preprocess_notes():
    # 🔹 Step 1: Sync notes from Joplin into raw folder
    print("Fetching latest notes from Joplin...")
    joplin_api.save_notes_to_disk()

    # 🔹 Step 2: Ensure processed folder exists
    os.makedirs(config.PROCESSED_DIR, exist_ok=True)

    # 🔹 Step 3: Process each markdown file
    files = os.listdir(config.RAW_DIR)
    if not files:
        print(f"No files found in RAW_DIR: {config.RAW_DIR}")
        return

    for fname in files:
        file_path = os.path.join(config.RAW_DIR, fname)
        if not fname.lower().endswith(".md"):
            print(f"Skipping non-markdown file: {fname}")
            continue

        with open(file_path, "r", encoding="utf-8") as f:
            raw_text = f.read()

        cleaned = clean_markdown(raw_text)
        chunks = chunk_text(cleaned)

        out_file = os.path.join(
            config.PROCESSED_DIR, fname.replace(".md", "_chunks.txt")
        )
        with open(out_file, "w", encoding="utf-8") as out:
            out.write("\n\n".join(chunks))

        print(f"Processed {fname} → {out_file}")

    print("✅ Preprocessing completed successfully!")

# Run the preprocessing if executed as a script
if __name__ == "__main__":
    preprocess_notes()

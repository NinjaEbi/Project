# src/config.py

# -------------------------------
# Joplin API
# -------------------------------
JOPLIN_BASE_URL = "http://127.0.0.1:41184"  # Ensure Joplin Web Clipper API is enabled
# Replace this with your actual token from Joplin Web Clipper options
JOPLIN_TOKEN = "715af483c5624e50edab76ab22867e46fe7c0620893ba0f438cefc6d3e0f8fcd30a3e28db80865eabadd8649938648135cfa23af65380998c39c78121c3278d1"

# -------------------------------
# File paths
# -------------------------------
RAW_DIR = "data/raw"
PROCESSED_DIR = "data/processed"
EMBEDDINGS_DIR = "embeddings"

# Absolute path to your GGUF model (update if needed)
MODEL_PATH = r"C:\Users\Niranjan\Desktop\joplin-ml-assistant\models\mistral-7b-instruct-v0.2.Q4_K_M.gguf"

# -------------------------------
# LLaMA settings
# -------------------------------
N_THREADS = 8  # Number of threads for model inference

# -------------------------------
# Chunking settings
# -------------------------------
CHUNK_SIZE = 500      # characters per chunk
CHUNK_OVERLAP = 50    # overlap between chunks

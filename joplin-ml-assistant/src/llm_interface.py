# src/llm_interface.py
import os
from llama_cpp import Llama
from src import config
from huggingface_hub import hf_hub_download

# -------------------------------
# 1️⃣ Ensure model exists
# -------------------------------
def get_model_path():
    # If MODEL_PATH exists, use it
    if os.path.exists(config.MODEL_PATH):
        return config.MODEL_PATH

    # Otherwise, download automatically
    print("Mistral GGUF model not found. Downloading...")
    model_cache_dir = os.path.join(os.path.expanduser("~"), "joplin_models")
    os.makedirs(model_cache_dir, exist_ok=True)

    model_file = hf_hub_download(
        repo_id="TheBloke/mistral-7B-Instruct-v0.2-GGUF",
        filename="mistral-7b-instruct-v0.2.Q4_K_M.gguf",
        cache_dir=model_cache_dir
    )
    print(f"✅ Model downloaded at: {model_file}")
    return model_file

# -------------------------------
# 2️⃣ Load the model
# -------------------------------
MODEL_PATH = get_model_path()
llm = Llama(model_path=MODEL_PATH, n_ctx=2048, n_threads=8)
print("✅ LLM loaded successfully!")

# -------------------------------
# 3️⃣ Function to run the LLM
# -------------------------------
def run_llm(prompt: str) -> str:
    output = llm(prompt, max_tokens=512, stop=["</s>"])
    return output["choices"][0]["text"].strip()

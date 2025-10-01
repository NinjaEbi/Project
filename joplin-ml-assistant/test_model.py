from llama_cpp import Llama
from src import config

llm = Llama(model_path=config.MODEL_PATH, n_ctx=2048, n_threads=config.N_THREADS)
print("✅ Model loaded successfully!")

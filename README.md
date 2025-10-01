# 📝 Joplin ML Assistant  

A lightweight **AI-powered summarizer and assistant** built on top of Joplin notes.  
This project integrates **Mistral-7B (GGUF via llama.cpp)** with embeddings and FAISS for semantic search.  

---

 Features
- Read notes directly from Joplin (via export/API)  
- Preprocess & chunk notes for efficient retrieval  
- Semantic search using FAISS + sentence-transformers  
- Local inference using **Mistral-7B GGUF**  
- Summarization and insights generated automatically  
- Simple **Streamlit UI** for interaction  
- Export results back into Joplin  

---

 Large File Download  

Some files (models, datasets, or demo videos) are too large for GitHub.  
You can access them here:  

Model File (Google Drive)  :

---
Installation  

```bash
# Clone the repository
git clone https://github.com/your-username/joplin-ml-assistant.git
cd joplin-ml-assistant

# Install dependencies
pip install -r requirements.txt

# Run the Streamlit UI
streamlit run src/ui.py

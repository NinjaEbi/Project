# src/ui.py
import sys
import os
import streamlit as st

# --- Fix import path ---
# Add project root (one level up from src/) to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Now imports will work
import summarizer
import joplin_api

# --- Streamlit App ---
st.set_page_config(page_title="Joplin Knowledge Assistant", page_icon="📒", layout="centered")

st.title("📒 Joplin Knowledge Assistant")
st.write("Ask questions about your Joplin notes and get AI-powered answers.")

# Input box
query = st.text_input("🔍 Ask a question about your notes:")

# Initialize session state for storing result
if "result" not in st.session_state:
    st.session_state.result = ""

# Search button
if st.button("Search"):
    if query.strip():
        try:
            # Get the answer from summarizer
            st.session_state.result = summarizer.answer_query(query)
        except Exception as e:
            st.error(f"⚠️ Error: {e}")
    else:
        st.warning("Please enter a question before searching.")

# Show the result if available
if st.session_state.result:
    st.markdown("### ✅ Answer")
    st.write(st.session_state.result)

    # Export to Joplin button
    if st.button("📤 Export to Joplin"):
        try:
            joplin_api.create_note("AI Generated Answer", st.session_state.result)
            st.success("Note exported to Joplin successfully!")
        except Exception as e:
            st.error(f"⚠️ Failed to export note: {e}")

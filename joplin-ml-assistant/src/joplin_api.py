# src/joplin_api.py
import requests
import os
from src import config

def fetch_notes():
    """Fetch all notes from Joplin API"""
    url = f"{config.JOPLIN_BASE_URL}/notes"
    params = {
        "token": config.JOPLIN_TOKEN,
        "fields": "id,title,body,updated_time"
    }
    resp = requests.get(url, params=params)
    resp.raise_for_status()
    data = resp.json()
    notes = data.get("items", [])
    return notes

def save_notes_to_disk():
    """Save all Joplin notes into data/raw as .md files"""
    notes = fetch_notes()
    os.makedirs(config.RAW_DIR, exist_ok=True)

    for note in notes:
        fname = f"{note['id']}.md"
        path = os.path.join(config.RAW_DIR, fname)
        with open(path, "w", encoding="utf-8") as f:
            f.write(f"# {note.get('title', 'Untitled')}\n\n")
            f.write(note.get("body", ""))
    print(f"✅ Saved {len(notes)} notes to {config.RAW_DIR}")

def create_note(title: str, body: str):
    """Create a new note in Joplin (e.g. for summaries)"""
    url = f"{config.JOPLIN_BASE_URL}/notes"
    params = {"token": config.JOPLIN_TOKEN}
    payload = {"title": title, "body": body}
    resp = requests.post(url, params=params, json=payload)
    resp.raise_for_status()
    print("✅ Note created in Joplin:", title)

if __name__ == "__main__":
    save_notes_to_disk()

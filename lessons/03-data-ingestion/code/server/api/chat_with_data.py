# server/api/chatbot.py
from models.data_ingestion import load_wikipedia_articles

def get_chatwithdata_response(message: str) -> str:
    chatbot = load_wikipedia_articles()
    # response = chatbot.invoke({"message": message})
    doc_count = chatbot
    return doc_count

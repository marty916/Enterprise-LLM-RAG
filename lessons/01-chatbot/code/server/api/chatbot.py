# server/api/chatbot.py
from models.langchain_model import setup_chatbot

def get_chatbot_response(message: str) -> str:
    chatbot = setup_chatbot()
    response = chatbot.invoke({"message": message})
    return response

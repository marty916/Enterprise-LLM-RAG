"""
/ server/api/chatbot.py

API endpoint to get chatbot response.

:param request: ChatRequest containing the user message.
:param service: ChatbotService instance.
:return: ChatResponse containing the chatbot's reply.
"""

from fastapi import APIRouter, Depends
from pydantic import BaseModel
from services.chatbot_service import ChatbotService
from models.langchain_model import ChatbotModel

router = APIRouter()

class ChatRequest(BaseModel):
    """
    Defines a Pydantic model for ChatRequest.

    Attributes:
        message (str): The user message for the chat request.
    """
    message: str

class ChatResponse(BaseModel):
    """
    Represents the response from the chatbot with the reply message.

    Attributes:
        reply (str): The chatbot's reply message.
    """
    reply: str

def get_chatbot_service() -> ChatbotService:
    """
    Dependency that provides a singleton instance of ChatbotService.
    """
    if not hasattr(get_chatbot_service, "service"):
        model = ChatbotModel()
        get_chatbot_service.service = ChatbotService(model)
    return get_chatbot_service.service

@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest, service: ChatbotService = Depends(get_chatbot_service)):
    """
    API endpoint to get chatbot response.

    :param request: ChatRequest containing the user message.
    :param service: ChatbotService instance.
    :return: ChatResponse containing the chatbot's reply.
    """
    response = service.get_response(request.message)
    return ChatResponse(reply=response)

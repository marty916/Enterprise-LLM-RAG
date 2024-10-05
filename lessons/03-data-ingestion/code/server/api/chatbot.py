# server/api/chatbot.py
from fastapi import APIRouter, Depends
from pydantic import BaseModel
from services.chatbot_service import ChatbotService
from models.langchain_model import GeneralChatbotModel

router = APIRouter()

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    reply: str

def get_general_chatbot_service() -> ChatbotService:
    """
    Dependency that provides a singleton instance of ChatbotService for general chat.
    """
    if not hasattr(get_general_chatbot_service, "service"):
        model = GeneralChatbotModel()
        get_general_chatbot_service.service = ChatbotService(model)
    return get_general_chatbot_service.service

@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest, service: ChatbotService = Depends(get_general_chatbot_service)):
    """
    API endpoint to get general chatbot response.

    :param request: ChatRequest containing the user message.
    :param service: ChatbotService instance for general chat.
    :return: ChatResponse containing the chatbot's reply.
    """
    response = service.get_response(request.message)
    return ChatResponse(reply=response)

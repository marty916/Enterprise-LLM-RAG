# server/api/customersupport.py
from fastapi import APIRouter, Depends
from pydantic import BaseModel
from services.customersupport_service import CustomerSupportService
from models.langchain_model import CustomerSupportChatbotModel

router = APIRouter()

class CustomerSupportRequest(BaseModel):
    message: str

class CustomerSupportResponse(BaseModel):
    reply: str

def get_customer_support_chatbot_service() -> CustomerSupportService:
    """
    Dependency that provides a singleton instance of CustomerSupportService for customer support.
    """
    if not hasattr(get_customer_support_chatbot_service, "service"):
        model = CustomerSupportChatbotModel()
        get_customer_support_chatbot_service.service = CustomerSupportService(model)
    return get_customer_support_chatbot_service.service

@router.post("/customer-support", response_model=CustomerSupportResponse)
async def customer_support_chat(request: CustomerSupportRequest, service: CustomerSupportService = Depends(get_customer_support_chatbot_service)):
    """
    API endpoint to get customer support chatbot response.

    :param request: CustomerSupportRequest containing the user message.
    :param service: CustomerSupportService instance for customer support chat.
    :return: CustomerSupportResponse containing the chatbot's reply.
    """
    response = service.get_response(request.message)
    return CustomerSupportResponse(reply=response)

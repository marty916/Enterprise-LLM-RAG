# server/services/customersupport_service.py
from models.langchain_model import IChatbotModel

class CustomerSupportService:
    """
    Service layer for customer support chatbot operations.
    """
    def __init__(self, model: IChatbotModel):
        self.model = model

    def get_response(self, message: str) -> str:
        """
        Gets a response from the customer support chatbot model.

        :param message: User message to the chatbot.
        :return: Chatbot's response as a string.
        """
        return self.model.invoke(message)

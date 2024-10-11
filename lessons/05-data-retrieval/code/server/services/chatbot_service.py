# server/services/chatbot_service.py
from models.langchain_model import IChatbotModel

class ChatbotService:
    """
    Service layer for general chatbot operations.
    """
    def __init__(self, model: IChatbotModel):
        self.model = model

    def get_response(self, message: str) -> str:
        """
        Gets a response from the chatbot model.

        :param message: User message to the chatbot.
        :return: Chatbot's response as a string.
        """
        return self.model.invoke(message)

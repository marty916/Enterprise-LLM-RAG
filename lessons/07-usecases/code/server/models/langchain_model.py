# server/models/langchain_model.py
from abc import ABC, abstractmethod
from models.index import ChatOpenAI, ChatPromptTemplate, StrOutputParser

class IChatbotModel(ABC):
    """
    Interface for chatbot models.
    """
    @abstractmethod
    def invoke(self, message: str) -> str:
        pass

class GeneralChatbotModel(IChatbotModel):
    """
    Concrete implementation of IChatbotModel for general chat.
    """
    def __init__(self, temperature: float = 0.7):
        self.model = ChatOpenAI(temperature=temperature)
        system_template = """
        You are a helpful assistant. Answer the following question.
        
        Question:
        """
        self.prompt_template = ChatPromptTemplate.from_messages(
            [("system", system_template), ("user", "{message}")]
        )
        self.parser = StrOutputParser()
        # Create a processing chain: prompt -> model -> parser
        self.chatbot = self.prompt_template | self.model | self.parser

    def invoke(self, message: str) -> str:
        """
        Invokes the general chatbot with the given message.

        :param message: User message to the chatbot.
        :return: Chatbot's response as a string.
        """
        return self.chatbot.invoke({"message": message})

class CustomerSupportChatbotModel(IChatbotModel):
    """
    Concrete implementation of IChatbotModel for customer support.
    """
    def __init__(self, temperature: float = 0.5):
        self.model = ChatOpenAI(temperature=temperature)
        system_template = """
        You are a customer support assistant. Help customers with their inquiries about our products and services.
        """
        self.prompt_template = ChatPromptTemplate.from_messages(
            [("system", system_template), ("user", "{message}")]
        )
        self.parser = StrOutputParser()
        # Create a processing chain: prompt -> model -> parser
        self.chatbot = self.prompt_template | self.model | self.parser

    def invoke(self, message: str) -> str:
        """
        Invokes the customer support chatbot with the given message.

        :param message: User message to the chatbot.
        :return: Chatbot's response as a string.
        """
        return self.chatbot.invoke({"message": message})

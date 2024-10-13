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
    def __init__(self, temperature: float = 0.7, model_name: str = "gpt-4o-2024-08-06"):
        self.model = ChatOpenAI(model=model_name, temperature=temperature)
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
    def __init__(self, temperature: float = 0.5, model_name: str = "gpt-4o-2024-08-06"):
        self.model = ChatOpenAI(model=model_name, temperature=temperature)
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

class ChatWithDataModel(IChatbotModel):
    """
    Model for ingesting data and retrieving embeddings.
    """
    def __init__(self, data_ingestion):
        self.data_ingestion = data_ingestion
        self.embeddings_data = None

    def invoke(self, message: str) -> str:
        """
        Not used in this context.
        """
        pass

    def ingest_and_get_embeddings(self) -> dict:
        """
        Performs data ingestion and retrieves embeddings data.
        """
        if not self.embeddings_data:
            self.embeddings_data = self.data_ingestion.load_data()
        return self.embeddings_data

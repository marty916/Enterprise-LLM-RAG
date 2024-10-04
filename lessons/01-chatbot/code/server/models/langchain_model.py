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

class ChatbotModel(IChatbotModel):
    """
    Concrete implementation of IChatbotModel using LangChain's ChatOpenAI.
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
        Invokes the chatbot with the given message.

        :param message: User message to the chatbot.
        :return: Chatbot's response as a string.
        """
        return self.chatbot.invoke({"message": message})

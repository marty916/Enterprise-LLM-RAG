# server/models/langchain_model.py
from abc import ABC, abstractmethod
from models.index import ChatOpenAI, ChatPromptTemplate, RunnablePassthrough, StrOutputParser
from models.vectorstore_singleton import VectorstoreSingleton

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

class ChatWithDataModel:
    """
    Model for ingesting data and retrieving embeddings using the vectorstore.
    """
    def __init__(self, data_ingestion):
        self.data_ingestion = data_ingestion
        self.vectorstore = None

    def ingest_and_get_embeddings(self) -> dict:
        """
        Performs data ingestion and retrieves embeddings data.
        """
        docs = self.data_ingestion.load_data()
        self.vectorstore = VectorstoreSingleton(docs)  # Initialize or use singleton for vectorstore
        embeddings = self.vectorstore.get_embeddings()  # Get embeddings
        metadata = self.data_ingestion.get_metadata(docs)  # Get metadata from the documents
        return {
            "embeddings": embeddings.tolist(),
            "metadata": metadata
        }
    
class ChatbotWithDocumentModel(IChatbotModel):
    """
    Concrete implementation of IChatbotModel for question-answering with retrieved documents.
    """
    def __init__(self, retriever, temperature: float = 0.7, model_name: str = "gpt-4o-2024-08-06"):
        self.model = ChatOpenAI(model=model_name, temperature=temperature)
        self.retriever = retriever
        self.prompt = ChatPromptTemplate.from_messages([
            ("human", """
            You are an assistant for question-answering tasks. Use the following pieces of retrieved context to answer the question. If you don't know the answer, just say that you don't know. Use three sentences maximum and keep the answer concise.
            Question: {question} 
            Context: {context} 
            Answer:""")
        ])
        self.parser = StrOutputParser()
        # Create a processing chain: retriever -> format_docs -> prompt -> model -> parser
        self.chatbot = (
            {"context": self.retriever | self.format_docs, "question": RunnablePassthrough()}
            | self.prompt 
            | self.model 
            | self.parser
        )

    @staticmethod
    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)
    
    def invoke(self, message: str) -> str:
        """
        Invokes the document-based chatbot with the given message.

        :param message: User message to the chatbot.
        :return: Chatbot's response as a string.
        """
        return self.chatbot.invoke({"question": message})


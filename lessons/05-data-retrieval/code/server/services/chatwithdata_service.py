# server/services/chatwithdata_service.py
from models.langchain_model import IChatbotModel

class ChatWithDataService:
    """
    Service layer for chat-with-data chatbot operations.
    """
    def __init__(self, model: IChatbotModel):
        self.model = model

    def ingest_and_get_embeddings(self) -> dict:
        """
        Performs data ingestion and returns embeddings data.
        """
        if hasattr(self.model, 'ingest_and_get_embeddings'):
            return self.model.ingest_and_get_embeddings()
        else:
            raise NotImplementedError("The model does not support ingestion and embeddings retrieval.")

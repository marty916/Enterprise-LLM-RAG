# server/api/chatwithdata.py
from fastapi import APIRouter, Depends
from pydantic import BaseModel
from services.chatwithdata_service import ChatWithDataService
from models.langchain_model import ChatWithDataModel
from models.data_ingestion import DocumentDataIngestion

router = APIRouter()

class ChatWithDataResponse(BaseModel):
    embeddings: list  # List of [x, y] coordinates
    metadata: list    # List of metadata dictionaries

def get_chatwithdata_service() -> ChatWithDataService:
    """
    Dependency that provides a singleton instance of ChatWithDataService for chat-with-data.
    """
    if not hasattr(get_chatwithdata_service, "service"):
        data_ingestion = DocumentDataIngestion()
        model = ChatWithDataModel(data_ingestion)
        get_chatwithdata_service.service = ChatWithDataService(model)
    return get_chatwithdata_service.service

@router.post("/chat-with-data", response_model=ChatWithDataResponse)
async def chat_with_data(service: ChatWithDataService = Depends(get_chatwithdata_service)):
    """
    API endpoint to ingest data and return embeddings for visualization.

    :param service: ChatWithDataService instance.
    :return: ChatWithDataResponse containing embeddings data and metadata.
    """
    embeddings_data = service.ingest_and_get_embeddings()
    return ChatWithDataResponse(**embeddings_data)

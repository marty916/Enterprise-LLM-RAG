# server/models/data_ingestion.py
from abc import ABC, abstractmethod
import os
from models.index import Docx2txtLoader

class IDataIngestion(ABC):
    """
    Interface for data ingestion processes.
    """
    @abstractmethod
    def load_data(self) -> dict:
        pass

class DocumentDataIngestion(IDataIngestion):
    """
    Concrete implementation of IDataIngestion for loading documents.
    """
    DOCUMENT_PATH = os.path.join("..", "..", "assets", "data", "Acme Bank FAQ.docx")

    def __init__(self, doc_path: str = DOCUMENT_PATH):
        self.doc_path = doc_path

    def load_data(self) -> dict:
        """
        Loads the documents from the given path.
        """
        docs = Docx2txtLoader(self.doc_path).load()
        return docs

    def get_metadata(self, docs) -> list:
        """
        Extract metadata from the loaded documents.
        """
        return [doc.metadata for doc in docs]

# server/models/data_ingestion.py
from abc import ABC, abstractmethod
from models.index import (
    Chroma, 
    OpenAIEmbeddings,
    Docx2txtLoader, 
    RecursiveCharacterTextSplitter
)
import numpy as np
from sklearn.decomposition import PCA
from core.config import settings
import os

class IDataIngestion(ABC):
    """
    Interface for data ingestion processes.
    """
    @abstractmethod
    def load_data(self) -> dict:
        pass

class DocumentDataIngestion(IDataIngestion):
    """
    Concrete implementation of IDataIngestion for loading Wikipedia articles.
    """
    DOCUMENT_PATH=os.path.join("..","..", "assets", "data", "Acme Bank FAQ.docx")
    def __init__(self, doc_path: str = DOCUMENT_PATH):
        self.doc_path = doc_path
        self.vectorstore = None

    def load_data(self) -> dict:
        docs = Docx2txtLoader(self.doc_path).load()
        self.vectorstore = self.save_to_vectorstore(docs)
        embeddings = self.get_embeddings()
        reduced_embeddings = self.reduce_dimensions(embeddings)
        metadata = self.get_metadata(docs)
        return {
            "embeddings": reduced_embeddings.tolist(),
            "metadata": metadata
        }

    def save_to_vectorstore(self, docs):
        # Change chunk size and overlap and see how the cluster chart changes
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        splits = text_splitter.split_documents(docs)
        vectorstore = Chroma.from_documents(documents=splits, embedding=OpenAIEmbeddings())
        return vectorstore

    def get_embeddings(self) -> np.ndarray:
        # Retrieve all embeddings from the vectorstore
        results = self.vectorstore.get(include=['embeddings'])
        embeddings_array = np.array(results['embeddings'])
        return embeddings_array

    def reduce_dimensions(self, embeddings: np.ndarray) -> np.ndarray:
        # Reduce embeddings to 2D using PCA for visualization
        pca = PCA(n_components=2)
        reduced = pca.fit_transform(embeddings)
        return reduced

    def get_metadata(self, docs) -> list:
        # Extract metadata (e.g., titles) from documents
        return [doc.metadata for doc in docs]

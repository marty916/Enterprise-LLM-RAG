# server/models/data_ingestion.py
from abc import ABC, abstractmethod
from models.index import (
    Chroma, 
    OpenAIEmbeddings, 
    WikipediaLoader, 
    RecursiveCharacterTextSplitter
)
import numpy as np
from sklearn.decomposition import PCA
from core.config import settings

class IDataIngestion(ABC):
    """
    Interface for data ingestion processes.
    """
    @abstractmethod
    def load_data(self) -> dict:
        pass

class WikipediaDataIngestion(IDataIngestion):
    """
    Concrete implementation of IDataIngestion for loading Wikipedia articles.
    """
    WIKIPEDIA_QUERY="Consitution of the United States"
    def __init__(self, query: str = WIKIPEDIA_QUERY, load_max_docs: int = 2):
        self.query = query
        self.load_max_docs = load_max_docs
        self.vectorstore = None

    def load_data(self) -> dict:
        docs = WikipediaLoader(query=self.query, load_max_docs=self.load_max_docs).load()
        print(f"Number of documents loaded: {len(docs)}")
        self.vectorstore = self.save_to_vectorstore(docs)
        embeddings = self.get_embeddings()
        reduced_embeddings = self.reduce_dimensions(embeddings)
        metadata = self.get_metadata(docs)
        return {
            "embeddings": reduced_embeddings.tolist(),
            "metadata": metadata
        }

    def save_to_vectorstore(self, docs):
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

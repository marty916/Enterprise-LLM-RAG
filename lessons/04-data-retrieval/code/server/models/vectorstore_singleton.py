# server/models/vectorstore_singleton.py
import numpy as np
from models.index import Chroma, OpenAIEmbeddings, RecursiveCharacterTextSplitter

class VectorstoreSingleton:
    _instance = None

    def __new__(cls, docs=None):
        if cls._instance is None and docs is not None:
            cls._instance = cls._initialize_vectorstore(docs)
        return cls._instance

    @classmethod
    def _initialize_vectorstore(cls, docs):
        """
        Initialize the vectorstore by splitting documents and embedding them.
        """
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        splits = text_splitter.split_documents(docs)
        vectorstore = Chroma.from_documents(documents=splits, embedding=OpenAIEmbeddings())
        return vectorstore

    def save_to_vectorstore(self, docs):
        """
        Save the provided documents to the vectorstore.
        """
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        splits = text_splitter.split_documents(docs)
        vectorstore = Chroma.from_documents(documents=splits, embedding=OpenAIEmbeddings())
        return vectorstore

    def get_embeddings(self):
        """
        Retrieve embeddings from the vectorstore.
        """
        results = self.vectorstore.get(include=['embeddings'])
        embeddings_array = np.array(results['embeddings'])
        return embeddings_array

    def get_retriever(self):
        """
        Return the retriever from the vectorstore.
        """
        return self.vectorstore.as_retriever()

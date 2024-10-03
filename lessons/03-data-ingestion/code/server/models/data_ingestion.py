# server/models/data_ingestion.py
from models.index import Chroma, OpenAIEmbeddings, WikipediaLoader, RecursiveCharacterTextSplitter

def load_wikipedia_articles():
    docs = WikipediaLoader(query="HUNTER X HUNTER", load_max_docs=2).load()
    print(len(docs))
    vectorstore = save_to_vectorstore(docs)
    return len(docs)

def save_to_vectorstore(docs):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    splits = text_splitter.split_documents(docs)
    vectorstore = Chroma.from_documents(documents=splits, embedding=OpenAIEmbeddings())
    return vectorstore


  
    
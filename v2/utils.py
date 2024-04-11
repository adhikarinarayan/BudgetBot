from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain_pinecone import PineconeVectorStore
from langchain_community.llms import GooglePalm
from dotenv import load_dotenv

import os

#API KEYS
load_dotenv()

index_name = ''


# Load pdf using langchain
def load_pdf(filepath):
    loader = PyPDFLoader(filepath)
    pages = loader.load()
    return pages

# documents to chunks
def chunk_data(docs,chunk_size=1000,chunk_overlap=200):
    text_splitter=RecursiveCharacterTextSplitter(chunk_size=chunk_size,chunk_overlap=chunk_overlap)
    doc=text_splitter.split_documents(docs)
    return doc


# chunks to embeddings and store to vector database -

def vector_store(pages,index_name=index_name):
    embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')
    docsearch = PineconeVectorStore.from_documents(documents = pages,embedding=embeddings, index_name='learnrag')
    return docsearch


def get_conversation_chain(vectorstore):
    llm =GooglePalm()
    memory = ConversationBufferMemory(memory_key='chat_history',return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever = vectorstore.as_retriever(),
        memory = memory)
    
    return conversation_chain
#==========================================================================================
# functions for the app.py 
#==========================================================================================
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.embeddings import GooglePalmEmbeddings
from langchain_community.llms import GooglePalm
from langchain_community.vectorstores import FAISS
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory

#load APIKEY
import os
from dotenv import load_dotenv
load_dotenv()
# ENTER THE API KEY HERE
os.environ['GOOGLE_API_KEY'] = " "

#Process single PDF
def get_pdf_text(pdf_docs):
    text = ""
    pdf_reader = PdfReader(pdf_docs)
    for page in pdf_reader.pages:
        text+=page.extract_text()
    return text

# for multiple pdf docs
def get_pdfs_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text+=page.extract_text()
    return text


# Text to chunks
def get_text_chunks(text):
    text_splitter = CharacterTextSplitter(
        separator = "\n",
        chunk_size = 1000,
        chunk_overlap = 300,
        length_function=len)
    chunks = text_splitter.split_text(text)
    return chunks



# Chunks to embedding and store them
def get_vector_store(text_chunks):
    embeddings = GooglePalmEmbeddings()
    vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
    return vector_store


# for chat feature and saving chat history
def get_conversation_chain(vectorstore):
    llm =GooglePalm()
    memory = ConversationBufferMemory(memory_key='chat_history',return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever = vectorstore.as_retriever(),
        memory = memory)
    
    return conversation_chain

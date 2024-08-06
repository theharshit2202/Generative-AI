import os
import streamlit as st
from langchain_groq import ChatGroq
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import 
from langchain_community.vectorstorses import FAISS  #vector_store_db
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_google_genai import GoogleGenerativeAIEmbeddings

from dotenv import load_dotenv
load_dotenv()

## laod the Groq and GOogle APi key from the .env file

groq_api_key = os.getenv("GROQ_API_KEY")
os.environ['GOGLE_API_KEY'] = os.getenv("GOOGLE_API_KEY")

st.title("Gemma Model Document Q&A")

llm = ChatGroq(groq_api_key=groq_api_key, model_name="Gemma-7b-it")

prompt = ChatPromptTemplate.from_template(
    """
Answer the questions based on the provided context only.
Please provide the most accurate response based on the question 
<context>
{context}
<context>
Questions:{input}
"""
)

def vector_embedding():
    if "vector" not in st.session_state:
        st.session_state.embeddings=GoogleGenerativeAIEmbeddings(model="models/embedding-001")
        

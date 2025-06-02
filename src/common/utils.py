import os
from typing import List, Dict, Any
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.schema.document import Document
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


def get_embeddings(model_name="sentence-transformers/all-MiniLM-L6-v2"):
    """
    Get HuggingFace embeddings using a smaller, faster model.
    """
    print(
        f"Loading embeddings model: {model_name} (this may take a moment the first time)")

    # Create embeddings model
    embeddings = HuggingFaceEmbeddings(
        model_name=model_name,
        model_kwargs={'device': 'cpu'},
        encode_kwargs={'normalize_embeddings': True}
    )

    print("Embeddings model loaded successfully!")
    return embeddings


def load_pdf(pdf_path: str) -> List[Document]:
    """
    Load a PDF file and return a list of Document objects
    """
    loader = PyPDFLoader(pdf_path)
    return loader.load()


def split_documents(documents: List[Document], chunk_size=1000, chunk_overlap=200) -> List[Document]:
    """
    Split documents into chunks for processing
    """
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=["\n\n", "\n", ".", " ", ""]
    )
    return text_splitter.split_documents(documents)


def create_vectorstore(documents: List[Document], persist_directory: str = None) -> FAISS:
    """
    Create a FAISS vectorstore from documents
    """
    # Get embeddings
    embeddings = get_embeddings()

    # Create and save the vectorstore
    vectorstore = FAISS.from_documents(documents, embeddings)

    # Save the vectorstore if a directory is provided
    if persist_directory:
        os.makedirs(persist_directory, exist_ok=True)
        vectorstore.save_local(persist_directory)

    return vectorstore


def load_vectorstore(persist_directory: str):
    """
    Load a FAISS vectorstore from disk
    """
    embeddings = get_embeddings()
    # Added allow_dangerous_deserialization to fix the pickle security error
    vectorstore = FAISS.load_local(persist_directory, embeddings,
                                   allow_dangerous_deserialization=True)
    return vectorstore

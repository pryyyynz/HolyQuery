from src.common.utils import load_pdf, split_documents, create_vectorstore
import os
import sys
from pathlib import Path

# Add the project root to path to enable imports
project_root = Path(__file__).parent
sys.path.append(str(project_root))


def initialize_vector_stores(force_reinit=False):
    """
    Initialize vector stores for both Bible and Quran

    Parameters:
    -----------
    force_reinit : bool, default=False
        If True, recreate the vector stores even if they already exist
    """
    # Create data directory if it doesn't exist
    os.makedirs(os.path.join(project_root, "data"), exist_ok=True)

    # Bible vector store
    bible_pdf_path = os.path.join(project_root, "scripts", "Bible.pdf")
    bible_vector_path = os.path.join(project_root, "data", "bible_vectorstore")

    if not os.path.exists(bible_vector_path) or force_reinit:
        print("Creating Bible vector store...")
        bible_docs = load_pdf(bible_pdf_path)
        bible_chunks = split_documents(bible_docs)
        create_vectorstore(bible_chunks, bible_vector_path)
        print(f"Bible vector store created at: {bible_vector_path}")
    else:
        print(f"Bible vector store already exists at: {bible_vector_path}")

    # Quran vector store
    quran_pdf_path = os.path.join(project_root, "scripts", "Quran.pdf")
    quran_vector_path = os.path.join(project_root, "data", "quran_vectorstore")

    if not os.path.exists(quran_vector_path) or force_reinit:
        print("Creating Quran vector store...")
        quran_docs = load_pdf(quran_pdf_path)
        quran_chunks = split_documents(quran_docs)
        create_vectorstore(quran_chunks, quran_vector_path)
        print(f"Quran vector store created at: {quran_vector_path}")
    else:
        print(f"Quran vector store already exists at: {quran_vector_path}")

    print("Vector stores initialization complete!")


if __name__ == "__main__":
    initialize_vector_stores()

from dotenv import load_dotenv
import anthropic
from langchain.prompts import PromptTemplate
from langchain.schema.runnable import RunnableMap
from langchain_core.runnables import RunnablePassthrough
from src.common.utils import load_pdf, split_documents, create_vectorstore, load_vectorstore
import os
import sys
from pathlib import Path

# Add the project root to path to enable imports
project_root = Path(__file__).parent.parent.parent
sys.path.append(str(project_root))

# Load environment variables
load_dotenv()


class QuranRAG:
    def __init__(self):
        self.vectorstore_path = os.path.join(
            project_root, "data", "quran_vectorstore")
        self.pdf_path = os.path.join(project_root, "scripts", "Quran.pdf")
        self.retriever = None

        # Initialize the Anthropic client
        self.client = anthropic.Anthropic(
            api_key=os.environ.get("CLAUDE_API_KEY"))

        # Initialize the RAG system
        self._initialize()

    def _initialize(self):
        """Initialize the Quran RAG system"""
        # Check if vectorstore exists, create if it doesn't
        if not os.path.exists(self.vectorstore_path):
            print("Creating Quran vectorstore...")
            documents = load_pdf(self.pdf_path)
            chunks = split_documents(documents)
            vectorstore = create_vectorstore(chunks, self.vectorstore_path)
            self.retriever = vectorstore.as_retriever(
                search_type="similarity",
                search_kwargs={"k": 5}
            )
        else:
            print("Loading existing Quran vectorstore...")
            vectorstore = load_vectorstore(self.vectorstore_path)
            self.retriever = vectorstore.as_retriever(
                search_type="similarity",
                search_kwargs={"k": 5}
            )

    def query(self, question: str) -> str:
        """
        Query the Quran RAG system
        """
        if not self.retriever:
            return "Error: RAG system not initialized"

        # Get relevant context from the retriever
        retrieved_docs = self.retriever.invoke(question)
        context = "\n\n".join([doc.page_content for doc in retrieved_docs])

        # Create the prompt with context
        prompt = f"""You are a helpful Quran scholar assistant with deep knowledge of Islamic texts, traditions, and interpretations.

        CONTEXT:
        {context}

        GUIDELINES FOR YOUR RESPONSE:
        1. Base your answer primarily on the provided context from the Quran
        2. If the context doesn't fully answer the question, indicate this clearly
        3. Ensure accuracy and respect when discussing Islamic scripture
        4. Include relevant verse references (Surah and Ayah numbers) when applicable
        5. When appropriate, mention the historical context or circumstances of revelation (asbab al-nuzul)
        6. Avoid personal interpretations that deviate from mainstream scholarly consensus
        7. Present diverse scholarly interpretations when relevant, noting which views are majority/minority positions
        8. Use precise theological terminology with explanations for those unfamiliar with Islamic concepts
        9. For complex topics, provide a simplified explanation followed by more nuanced details
        10. Acknowledge limitations in your answer when the question requires specialized expertise

        Question: {question}
        
        Answer (structure your response clearly with appropriate headings when needed):"""

        # Query Claude
        message = self.client.messages.create(
            model="claude-3-opus-20240229",
            max_tokens=1000,
            temperature=0.5,
            messages=[{"role": "user", "content": prompt}]
        )

        return message.content[0].text

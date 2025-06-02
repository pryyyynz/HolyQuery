from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain.schema.runnable import RunnableMap
from langchain_core.runnables import RunnablePassthrough
from src.common.utils import load_pdf, split_documents, create_vectorstore, load_vectorstore
import os
import sys
from pathlib import Path
import anthropic

# Add the project root to path to enable imports
project_root = Path(__file__).parent.parent.parent
sys.path.append(str(project_root))


# Load environment variables
load_dotenv()


class BibleRAG:
    def __init__(self):
        self.vectorstore_path = os.path.join(
            project_root, "data", "bible_vectorstore")
        self.pdf_path = os.path.join(project_root, "scripts", "Bible.pdf")
        self.retriever = None

        # Initialize the Anthropic client
        self.client = anthropic.Anthropic(
            api_key=os.environ.get("CLAUDE_API_KEY"))

        # Initialize the RAG system
        self._initialize()

    def _initialize(self):
        """Initialize the Bible RAG system"""
        # Check if vectorstore exists, create if it doesn't
        if not os.path.exists(self.vectorstore_path):
            print("Creating Bible vectorstore...")
            documents = load_pdf(self.pdf_path)
            chunks = split_documents(documents)
            vectorstore = create_vectorstore(chunks, self.vectorstore_path)
            self.retriever = vectorstore.as_retriever(
                search_type="similarity",
                search_kwargs={"k": 5}
            )
        else:
            print("Loading existing Bible vectorstore...")
            vectorstore = load_vectorstore(self.vectorstore_path)
            self.retriever = vectorstore.as_retriever(
                search_type="similarity",
                search_kwargs={"k": 5}
            )

    def query(self, question: str) -> str:
        """
        Query the Bible RAG system
        """
        if not self.retriever:
            return "Error: RAG system not initialized"

        # Get relevant context from the retriever
        retrieved_docs = self.retriever.invoke(question)
        context = "\n\n".join([doc.page_content for doc in retrieved_docs])

        # Create the prompt with context
        prompt = f"""You are a helpful Bible scholar assistant with deep knowledge of Biblical texts, traditions, exegesis, and hermeneutics.

        CONTEXT FROM THE BIBLE:
        {context}

        GUIDELINES FOR YOUR RESPONSE:
        1. Base your answer primarily on the provided Biblical context
        2. If the context doesn't fully answer the question, indicate this clearly
        3. Include relevant Bible references (book, chapter, verse) when applicable
        4. When appropriate, provide historical and cultural context for proper understanding
        5. Present different theological interpretations when relevant (e.g., Catholic, Protestant, Orthodox perspectives)
        6. Use precise theological terminology with explanations for those unfamiliar with Biblical concepts
        7. For complex topics, provide a simplified explanation followed by more nuanced details
        8. When addressing controversial topics, present multiple viewpoints in a balanced manner
        9. Consider both literal and metaphorical/allegorical interpretations where appropriate
        10. Acknowledge when scholarly consensus is divided on particular interpretations
        11. Be respectful of diverse faith traditions while maintaining scholarly accuracy
        12. For questions about Biblical languages, provide insights about Hebrew, Greek, or Aramaic terms when relevant

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

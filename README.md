# HolyQuery

![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)
![Python](https://img.shields.io/badge/python-3.9%2B-blue)

HolyQuery is an interactive RAG (Retrieval-Augmented Generation) system that allows users to query the Bible and Quran for insights, interpretations, and knowledge. Powered by Anthropic's Claude AI model, it provides contextually relevant and thoughtful answers based on these sacred texts.

## Live Application

Check out the live application: [HolyQuery](https://holyquery.streamlit.app/)

## ✨ Features

- **Dual Text Support**: Search and query both the Bible and Quran from a single interface
- **Contextual Answers**: Get responses that include relevant passages and context from the sacred texts
- **Vector-based Retrieval**: Utilizes vector embeddings for semantic search capabilities

## 📋 Requirements

- Python 3.9+
- Anthropic API key (Claude model)
- Dependencies listed in `requirements.txt`

## 🛠️ Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/HolyQuery.git
cd HolyQuery

# Install dependencies
pip install -r requirements.txt

# Create .env file and add your Anthropic API key
echo "CLAUDE_API_KEY=your_api_key_here" > .env
```

## 🚀 Usage

1. **Initialize the vector stores** (optional, will be created on first run if they don't exist):
    ```bash
    python initialize_rag.py
    ```

2. **Run the application**:
    ```bash
    streamlit run app.py
    ```

3. **Access the web interface** at http://localhost:8501

4. **Ask questions** in either the Bible or Quran tab to receive AI-generated answers based on the sacred texts

## 📊 Project Structure

```
HolyQuery/
├── app.py                   # Main Streamlit application
├── initialize_rag.py        # Script to initialize vector stores
├── requirements.txt         # Python dependencies
├── data/                    # Vector store data
│   ├── bible_vectorstore/   # FAISS vector index for Bible
│   └── quran_vectorstore/   # FAISS vector index for Quran
├── scripts/                 # Source PDF files
│   ├── Bible.pdf            # Bible text
│   └── Quran.pdf            # Quran text
└── src/                     # Source code
    ├── bible/               # Bible RAG implementation
    ├── common/              # Shared utilities
    └── quran/               # Quran RAG implementation
```


# HolyQuery

![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)
![Python](https://img.shields.io/badge/python-3.9%2B-blue)

HolyQuery is an interactive RAG (Retrieval-Augmented Generation) system that allows users to query the Bible and Quran for insights, interpretations, and knowledge. Powered by Anthropic's Claude AI model, it provides contextually relevant and thoughtful answers based on these sacred texts.

## ✨ Features

- **Dual Text Support**: Search and query both the Bible and Quran from a single interface
- **Contextual Answers**: Get responses that include relevant passages and context from the sacred texts
- **User-friendly Interface**: Simple, intuitive Streamlit web interface
- **Scholarly Approach**: Responses follow scholarly guidelines for interpreting religious texts
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

## ⚙️ Configuration

### Environment Variables

Create a `.env` file in the project root:

```
CLAUDE_API_KEY=your_anthropic_api_key_here
```

### Streamlit Cloud Deployment

For Streamlit Cloud deployment, add the `CLAUDE_API_KEY` to your secrets in the Streamlit Cloud dashboard.

## 🎨 Customization

- **Model Parameters**: You can adjust temperature, max_tokens, and other parameters in the RAG classes
- **UI Styling**: Modify the CSS in `app.py` to customize the appearance
- **RAG Settings**: Adjust retrieval settings (k value, etc.) in the RAG classes

## 📝 Notes for Dark Mode Users

The application supports both light and dark mode. If you encounter any display issues in dark mode, try switching to light mode or refresh the page.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- Anthropic for the Claude AI model
- The Streamlit team for their excellent framework
- All contributors and supporters of the project

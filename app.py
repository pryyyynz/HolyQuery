from src.quran.quran_rag import QuranRAG
from src.bible.bible_rag import BibleRAG
import streamlit as st
import time
import os
import sys
from pathlib import Path

# Add the project root to path to enable imports
project_root = Path(__file__).parent
sys.path.append(str(project_root))


# Page configuration
st.set_page_config(
    page_title="Holy Query - Bible & Quran RAG System",
    page_icon="📚",
    layout="wide",
)

# Apply custom styling
st.markdown("""
<style>
    .main {
        background-color: #f5f5f5;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 2px;
        background-color: white;
    }
    .stTabs [data-baseweb="tab"] {
        height: 60px;
        white-space: pre-wrap;
        background-color: #f0f0f0;
        border-radius: 4px 4px 0px 0px;
        gap: 1px;
        padding: 10px 16px;
        font-size: 16px;
    }
    .stTabs [aria-selected="true"] {
        background-color: #4169E1;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# Title
st.title("📚 Holy Query")
st.subheader("Interactive Bible & Quran System")

# Session state initialization
if 'bible_rag' not in st.session_state:
    with st.spinner('Initializing Bible system...'):
        st.session_state.bible_rag = BibleRAG()

if 'quran_rag' not in st.session_state:
    with st.spinner('Initializing Quran system...'):
        st.session_state.quran_rag = QuranRAG()

# Create tabs
tab1, tab2 = st.tabs(["Bible Query", "Quran Query"])

# Bible Tab
with tab1:
    st.header("Bible Query")
    st.markdown("""
    Ask questions about the Bible and receive answers backed by the biblical text.
    The system will retrieve relevant passages and provide contextual information.
    """)

    # Query input
    bible_query = st.text_input(
        "Enter your Bible question:",
        key="bible_input",
        placeholder="For example: What does the Bible say about forgiveness?"
    )

    # Process query
    if bible_query:
        with st.spinner('Searching the Bible for answers...'):
            bible_answer = st.session_state.bible_rag.query(bible_query)

        # Display answer
        st.subheader("Answer")
        st.markdown(bible_answer)

# Quran Tab
with tab2:
    st.header("Quran Query")
    st.markdown("""
    Ask questions about the Quran and receive answers backed by the Quranic text.
    The system will retrieve relevant passages and provide contextual information.
    """)

    # Query input
    quran_query = st.text_input(
        "Enter your Quran question:",
        key="quran_input",
        placeholder="For example: What does the Quran teach about charity?"
    )

    # Process query
    if quran_query:
        with st.spinner('Searching the Quran for answers...'):
            quran_answer = st.session_state.quran_rag.query(quran_query)

        # Display answer
        st.subheader("Answer")
        st.markdown(quran_answer)

# Footer
st.markdown("""
---
### About
Holy Query is designed to deepen your spiritual journey by providing thoughtful answers to your questions about sacred texts. Whether you're exploring the Bible's wisdom or the Quran's guidance, this tool helps you:

- Gain deeper understanding of spiritual teachings and principles
- Find comfort and direction through sacred wisdom
- Compare perspectives across different passages and contexts
- Develop a more personal connection with religious texts
- Apply timeless spiritual insights to modern life challenges

Our mission is to make divine wisdom more accessible to all seekers, regardless of your level of religious knowledge or background. We hope this tool supports your spiritual growth and personal reflection.
""")

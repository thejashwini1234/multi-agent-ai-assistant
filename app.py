import streamlit as st
import os

from rag.loader import load_pdf
from rag.splitter import split_text
from rag.embeddings import get_embeddings
from rag.vector_store import VectorStore

from agents.manager_agent import manager_agent
from agents.sql_agent import run_query

st.title("Enterprise AI Knowledge Assistant")

# =========================
# PDF Upload
# =========================

uploaded_file = st.file_uploader(
    "Upload PDF",
    type=["pdf"]
)

vectorstore = None

if uploaded_file:

    path = os.path.join(
        "uploads",
        uploaded_file.name
    )

    with open(path, "wb") as f:

        f.write(
            uploaded_file.getbuffer()
        )

    text = load_pdf(path)

    chunks = split_text(text)

    embeddings = get_embeddings(chunks)

    vectorstore = VectorStore()

    vectorstore.add_embeddings(
        chunks,
        embeddings
    )

    st.success("Document processed")

# =========================
# RAG QUESTION SECTION
# =========================

st.header("Ask Questions From Document")

query = st.text_input(
    "Ask document question"
)

if st.button("Ask Document"):

    if vectorstore:

        result = manager_agent(
            query,
            vectorstore
        )

        st.write(result["response"])

# =========================
# SQL SECTION
# =========================

st.header("SQL Agent")

sql_query = st.text_area(
    "Enter SQL Query"
)

if st.button("Run SQL Query"):

    result = run_query(
        sql_query
    )

    st.write(result)
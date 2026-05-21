import streamlit as st
from langchain_groq import ChatGroq

from rag.embeddings import embed_query

def retrieval_agent(
    vectorstore,
    query
):

    query_embedding = embed_query(
        query
    )

    docs = vectorstore.search(
        query_embedding
    )

    context = "\n".join(docs)

    prompt = f"""
    Answer the question using the context below.

    Context:
    {context}

    Question:
    {query}

    Answer:
    """

    llm = ChatGroq(
    api_key=st.secrets["GROQ_API_KEY"],
    model_name="llama3-8b-8192"
)

    response = llm.invoke(prompt)

    return response.content
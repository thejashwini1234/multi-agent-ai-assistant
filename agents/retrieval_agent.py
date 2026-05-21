from dotenv import load_dotenv
from langchain_groq import ChatGroq

from rag.embeddings import embed_query

load_dotenv()

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
        model_name="llama-3.3-70b-versatile"
    )

    response = llm.invoke(prompt)

    return response.content
Multi-Agent AI Enterprise Assistant

An AI-powered Enterprise Knowledge Assistant built using RAG (Retrieval-Augmented Generation), Multi-Agent Architecture, Streamlit, FAISS, Groq LLM, and MySQL.

Live Demo

🚀 Deployed Application:

[Multi-Agent AI Assistant App](https://multi-agent-ai-assistant-ihcysubncvnha7bh8amrd9.streamlit.app/)

Features

📄 Upload PDF documents

🤖 Ask questions from uploaded documents

🔍 Semantic search using FAISS vector database

🧠 LLM-powered responses using Groq + Llama 3

🗂️ Multi-Agent AI Architecture

🛢️ SQL Query Agent for database interaction

✅ Response validation system

📊 Enterprise-style AI assistant interface

Tech Stack

Frontend

Streamlit

Backend

Python

AI & NLP

LangChain

Groq API

Llama 3.1

RAG Architecture

Vector Database

FAISS

Embeddings

Scikit-learn TF-IDF Vectorizer

Database

MySQL

SQLAlchemy

Railway Cloud Database

Project Architecture

User Query

     ↓
     
Manager Agent

     ↓
     
Retrieval Agent

     ↓
FAISS Vector Search

     ↓
     
Groq LLM Response

     ↓
     
Validation Agent

     ↓
     
Final Response

Folder Structure

multi-agent-ai-assistant/

│
├── agents/

│   ├── manager_agent.py

│   ├── retrieval_agent.py

│   ├── sql_agent.py

│   ├── validation_agent.py

│   └── report_agent.py

│
├── rag/

│   ├── loader.py

│   ├── splitter.py

│   ├── embeddings.py

│   └── vector_store.py
│
├── database/

│   └── db.py
│
├── uploads/
│
├── app.py

├── requirements.txt

└── README.md

Installation

Clone Repository

git clone https://github.com/thejashwini1234/multi-agent-ai-assistant.git

Move to Project Folder

cd multi-agent-ai-assistant

Install Requirements

pip install -r requirements.txt

Environment Variables

Create a .streamlit/secrets.toml file:

GROQ_API_KEY = "your_groq_api_key"

DATABASE_URL = "your_mysql_database_url"

Run Application

streamlit run app.py

How It Works

User uploads a PDF document

Text is extracted from the PDF

Text is split into chunks

TF-IDF embeddings are generated

Embeddings are stored in FAISS

Relevant chunks are retrieved based on user query

Groq LLM generates contextual response

Validation agent checks output quality


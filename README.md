# Medical RAG System

A Retrieval-Augmented Generation (RAG) system built with Python, FastAPI, PostgreSQL (pgvector), and integrated with the Igentic AI Agent.

## Features

- PDF ingestion
- Text chunking
- Sentence embeddings (BAAI/bge-small-en-v1.5)
- PostgreSQL + pgvector vector storage
- Semantic similarity search
- FastAPI Retrieval API
- Igentic AI Agent integration

## Tech Stack

- Python
- FastAPI
- PostgreSQL
- pgvector
- Sentence Transformers
- PyMuPDF
- LangChain Text Splitters
- Neon Database
- GPT-5.4 (via Igentic)

## Project Structure

```
Medical-RAG/
│
├── data/
├── scripts/
├── services/
├── tests/
├── tools/
├── db.py
├── .env
├── README.md
```

## Run

Install dependencies

```bash
pip install -r requirements.txt
```

Run ingestion

```bash
python scripts/ingest.py
```

Run API

```bash
uvicorn app:app --reload
```

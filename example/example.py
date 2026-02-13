#!/usr/bin/env python3
"""
RAG Tutorial 05 — Your First RAG Pipeline
Minimal example: load text → chunk → embed → store → retrieve → generate (mock LLM).
Run: pip install -r requirements.txt && python example.py
"""
import chromadb
from chromadb.config import Settings
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")


def chunk(text: str, size: int = 150) -> list[str]:
    return [text[i : i + size].strip() for i in range(0, len(text), size) if text[i : i + size].strip()]


def mock_llm(query: str, context: str) -> str:
    """Simulate LLM: return a short answer that cites the context."""
    return f"Based on the context: {context[:100]}... [Answer would address: {query}]"


def main():
    # 1. "Load" document
    doc = (
        "RAG stands for Retrieval-Augmented Generation. "
        "You retrieve relevant chunks from a vector store, then pass them as context to an LLM. "
        "The LLM generates an answer grounded in your documents."
    )
    # 2. Chunk
    chunks = chunk(doc)
    # 3. Embed & store
    client = chromadb.Client(Settings(anonymized_telemetry=False))
    coll = client.get_or_create_collection("rag05_example")
    embeddings = model.encode(chunks).tolist()
    coll.add(ids=[f"c_{i}" for i in range(len(chunks))], embeddings=embeddings, documents=chunks)
    # 4. Query: retrieve
    query = "What is RAG?"
    q_emb = model.encode([query]).tolist()
    results = coll.query(query_embeddings=q_emb, n_results=2, include=["documents"])
    context = " ".join(results["documents"][0])
    # 5. Generate
    answer = mock_llm(query, context)
    print("Query:", query)
    print("Retrieved context:", context[:120] + "...")
    print("Answer:", answer)


if __name__ == "__main__":
    main()

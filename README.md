# 🎯 RAG Tutorial 05 — Your First RAG Pipeline

<p align="center">
  <a href="https://github.com/kishore2797/mastering-rag"><img src="https://img.shields.io/badge/Series-Mastering_RAG-blue?style=for-the-badge" /></a>
  <img src="https://img.shields.io/badge/Part-5_of_16-green?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Difficulty-Intermediate-yellow?style=for-the-badge" />
</p>

> **Part of the [Mastering RAG](https://github.com/kishore2797/mastering-rag) tutorial series**  
> Previous: [04 — Vector Stores](https://github.com/kishore2797/rag-04-vector-stores) | Next: [06 — Wikipedia Chatbot](https://github.com/kishore2797/rag-06-wikipedia-chatbot)

---

## 🌍 Real-World Scenario

> A startup has 200 investor reports as PDFs. The CEO asks: "What did we tell investors about churn in Q3?" Nobody wants to ctrl+F through 200 files. With this RAG pipeline, the CEO uploads the reports, asks the question in plain English, and gets: *"In the Q3 investor update (page 7), churn was reported at 4.2%, down from 5.1% in Q2, attributed to the new onboarding flow."* — with a link to the exact source.

---

## 🏗️ What You'll Build

A complete document Q&A system that wires together every foundation tutorial: **load documents, chunk them, embed, store in a vector DB, retrieve relevant chunks, and generate answers with an LLM** — all with source citations.

```
Upload PDF ──→ Chunk ──→ Embed ──→ Store (ChromaDB)
                                        ↓
"What was Q3 revenue?" ──→ Retrieve top-K ──→ LLM + Context ──→ Answer with sources
```

## 🔑 Key Concepts

- **End-to-end RAG pipeline**: the complete flow from document to answer
- **Prompt engineering for RAG**: system prompts, context injection, citation instructions
- **Source attribution**: every answer cites which documents/chunks informed it
- **"I don't know" handling**: refuse gracefully when context is insufficient
- **Context window management**: fit the right amount of context for the LLM

## 🛠 Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python 3.11+ · FastAPI · ChromaDB · HuggingFace Embeddings · OpenAI/Gemini |
| Frontend | React 19 · Vite · Tailwind CSS |

## 🚀 Quick Start

### Backend

```bash
cd backend
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # Add your LLM API key
uvicorn app.main:app --reload --port 8000
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

Open http://localhost:5173 — upload documents, ask questions, get cited answers.

## 📦 Example

A minimal runnable example is in the `example/` folder:

```bash
cd example
pip install -r requirements.txt
python example.py
```

It wires load → chunk → embed → store → retrieve → generate (with a mock LLM).

## 📖 What You'll Learn

1. How to wire load → chunk → embed → store → retrieve → generate
2. Prompt engineering techniques specific to RAG
3. How to make the LLM cite its sources
4. When and how the system should say "I don't know"
5. Temperature and generation settings for factual accuracy

## 📋 Prerequisites

- Python 3.11+ and Node.js 18+
- Concepts from Tutorials 01–04 (document loading, chunking, embeddings, vector stores)
- An LLM API key (OpenAI, Gemini, or run Ollama locally)

## ✏️ Exercises

1. **Prompt engineering**: Change the system prompt to make the LLM respond in bullet points, or in a specific persona (e.g., "You are a financial analyst"). How does the output quality change?
2. **Top-K experiment**: Set K=1, K=3, K=5, K=10. For a fixed question, how does answer quality change? At what K does it start to degrade (too much noise)?
3. **"I don't know" test**: Ask a question about a topic NOT in your documents. Does the system refuse gracefully or hallucinate?
4. **Source verification**: For 5 questions, manually check if the cited sources actually contain the claimed information (this is faithfulness testing — you'll automate it in Tutorial 13)
5. **Multi-document**: Upload docs from two very different domains (e.g., a recipe book + a technical manual). Ask a question that spans both. How does the system handle it?

## ⚠️ Common Mistakes

| Mistake | Why It Happens | How to Fix |
|---------|---------------|------------|
| LLM ignores the retrieved context | Prompt doesn't emphasize "answer ONLY from the provided context" | Add explicit instructions: "If the context doesn't contain the answer, say 'I don't know'" |
| Citations point to wrong chunks | Chunk IDs get mixed up when formatting the prompt | Pass chunk metadata (source, page) alongside the text, and instruct the LLM to cite them |
| Answers are too long/verbose | Default temperature is high; no length constraint | Set temperature=0.1–0.3 for factual RAG; add "be concise" to the prompt |
| System crashes on large PDFs | All chunks sent to the LLM exceed context window | Limit to top-K chunks that fit within 80% of the context window |

## 📚 Further Reading

- [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://arxiv.org/abs/2005.11401) — The original RAG paper (Lewis et al., 2020)
- [Prompt Engineering Guide](https://www.promptingguide.ai/) — Techniques for better LLM prompts
- [LangChain RAG Tutorial](https://python.langchain.com/docs/tutorials/rag/) — Framework approach (compare with our from-scratch approach)
- [OpenAI Best Practices for RAG](https://platform.openai.com/docs/guides/prompt-engineering) — Official guidance

## ➡️ Next Steps

You've built a basic RAG pipeline. Head to **[Tutorial 06 — Wikipedia Chatbot](https://github.com/kishore2797/rag-06-wikipedia-chatbot)** to see RAG applied to live, dynamic data sources.

---

<p align="center">
  <sub>Part of <a href="https://github.com/kishore2797/mastering-rag">Mastering RAG — From Zero to Production</a></sub>
</p>

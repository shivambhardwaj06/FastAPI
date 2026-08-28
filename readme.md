# ⚡ Production FastAPI for ML, GenAI & Agentic Systems

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.110+-009688.svg?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![Pydantic v2](https://img.shields.io/badge/Pydantic-v2-E92063.svg?logo=pydantic&logoColor=white)](https://docs.pydantic.dev/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> **Moving beyond generic CRUD apps.** This repository houses practical architectures, patterns, and production-grade implementations for serving **Machine Learning inference, GenAI pipelines, and autonomous AI agents** using FastAPI.

---

## 🧭 Why This Exists

Most FastAPI tutorials stop at basic Todo apps and SQL CRUD. Real-world AI backends deal with different challenges:
- High-concurrency I/O vs. CPU-bound model inference
- Real-time streaming (SSE & WebSockets) for LLMs
- State management for multi-step agentic workflows
- Async queues for long-running batch predictions

This repo documents the transition from **core backend foundations** to **scalable AI serving infrastructure**.

---

## 🏛️ System Architecture

```text
┌─────────────────────────────────────────────────────────────┐
│                       Client Layer                          │
│          (Web Apps / Mobile / AI Agents / SDKs)             │
└──────────────────────────────┬──────────────────────────────┘
                               │  HTTPS / WSS / SSE
                               ▼
┌─────────────────────────────────────────────────────────────┐
│                      FastAPI Gateway                        │
│  ├── Auth & Rate Limiting (JWT / OAuth2 / Redis)            │
│  ├── Pydantic V2 Validation & Serialization                 │
│  └── Dependency Injection (Sessions, Clients, Singletons)   │
└──────────────┬─────────────────┬───────────────────┬────────┘
               │                 │                   │
    ┌──────────▼─────────┐ ┌─────▼──────────┐ ┌──────▼────────┐
    │ Persistence Layer  │ │ Inference Hub  │ │ GenAI Engine  │
    │  • PostgreSQL      │ │  • ONNX / PyTorch│ │  • LangChain  │
    │  • SQLAlchemy 2.0  │ │  • ThreadPool  │ │  • LlamaIndex │
    │  • Vector DBs      │ │  • Batching    │ │  • SSE Streams│
    └────────────────────┘ └────────────────┘ └───────────────┘

```

---

## 🗺️ Learning & Implementation Roadmap

```
├── 🟢 Phase 1: Production Core
│   ├── [x] Pydantic V2 schemas & deep validation
│   ├── [x] Dependency injection patterns (DB sessions, auth guards)
│   ├── [ ] Global exception handling & standardized RFC-7807 responses
│   └── [ ] Structured logging with Loguru & OpenTelemetry
│
├── 🟡 Phase 2: High-Performance Data & State
│   ├── [ ] Async SQLAlchemy 2.0 + Alembic migrations
│   ├── [ ] PostgreSQL connection pooling & session management
│   ├── [ ] Redis caching & distributed token-bucket rate limiting
│   └── [ ] Background processing (FastAPI native tasks vs. Celery/ARQ)
│
├── 🟣 Phase 3: ML Model Serving
│   ├── [ ] Non-blocking CPU inference using `run_in_threadpool`
│   ├── [ ] Model warm-up & lifespan event management
│   ├── [ ] Dynamic batching for PyTorch / ONNX models
│   └── [ ] Micro-benchmarking latency (p95 / p99) under load
│
└── 🔴 Phase 4: GenAI & Agentic Backends
    ├── [ ] Server-Sent Events (SSE) for token-by-token LLM streaming
    ├── [ ] Async Vector DB integration (pgvector / Qdrant / Pinecone)
    ├── [ ] RAG pipelines with semantic caching
    └── [ ] Multi-turn stateful Agent execution with WebSockets & Human-in-the-Loop

```

---

## 📂 Project Structure

```bash
fastapi-ai-backend/
├── app/
│   ├── api/
│   │   └── v1/
│   │       ├── endpoints/
│   │       │   ├── auth.py          # Authentication & Tokens
│   │       │   ├── inference.py     # Classical ML prediction routes
│   │       │   ├── rag.py           # Vector search & RAG endpoints
│   │       │   └── stream.py        # Token-level LLM streaming
│   │       └── router.py            # API router registry
│   ├── core/
│   │   ├── config.py                # Pydantic BaseSettings & env configs
│   │   ├── dependencies.py          # Reusable DI providers
│   │   └── security.py              # Cryptography & Token helpers
│   ├── models/                      # SQLAlchemy & Vector DB tables
│   ├── schemas/                     # Pydantic request/response schemas
│   ├── services/                    # Business logic (ML runtimes, LLM wrappers)
│   └── main.py                      # Application lifespan & entry point
├── tests/                           # Async test suite (pytest-asyncio + httpx)
├── .env.example
├── Dockerfile
└── pyproject.toml

```

---

## ⚡ Quickstart

### Prerequisites

* Python 3.10+
* [uv](https://github.com/astral-sh/uv) or `poetry` (recommended)

### Installation

```bash
# 1. Clone the repository
git clone [https://github.com/your-username/fastapi-ai-backend.git](https://github.com/your-username/fastapi-ai-backend.git)
cd fastapi-ai-backend

# 2. Set up virtual environment & install dependencies
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt

# 3. Configure environment variables
cp .env.example .env

# 4. Start the development server
uvicorn app.main:app --reload --port 8000

```

### Interactive Documentation

Once running, explore the interactive documentation:

* **Swagger UI:** [http://127.0.0.1:8000/docs](https://www.google.com/search?q=http://127.0.0.1:8000/docs)
* **Scalar / ReDoc:** [http://127.0.0.1:8000/redoc](https://www.google.com/search?q=http://127.0.0.1:8000/redoc)

---

## 🧪 Experiments & Benchmarks

| Milestone | Target | Tech Stack | Status |
| --- | --- | --- | --- |
| **01_pydantic_validation** | Request parsing & nested schemas | Pydantic V2 | 🟢 Done |
| **02_async_sqlalchemy** | Non-blocking async DB sessions | SQLAlchemy 2.0 + asyncpg | 🟡 In Progress |
| **03_onnx_inference** | Real-time classification API | ONNX Runtime + ThreadPool | ⚪ Planned |
| **04_llm_streaming** | Token streaming using SSE | FastAPI + LangChain / OpenAI | ⚪ Planned |
| **05_agent_orchestration** | Autonomous agent step execution | LangGraph + WebSockets | ⚪ Planned |

---

## 🤝 Contributing & Feedback

This is an open learning journey. If you spot anti-patterns, bottlenecks, or areas for performance optimization, feel free to open an **Issue** or submit a **Pull Request**.

---
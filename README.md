<div align="center">
  <img src="https://raw.githubusercontent.com/franamaro-dev/VeriStack/main/.assets/header.jpg" width="100%" alt="VeriStack Banner">
</div>

# VeriStack

> **Zero-trust RAG architecture for strict financial compliance.**

VeriStack provides a self-hosted, async-first backend to validate PKCS12 certificates and process financial documents (TicketBAI / VeriFactu) using local vector embeddings. Zero data leaks. Sub-second latency.

## ⚠️ The Problem
Building AI-driven financial pipelines exposes critical vulnerabilities:
- **Data Sovereignty Violations:** Sending local tax invoices to third-party APIs (OpenAI, Anthropic) breaks strict European compliance.
- **Latency Overheads:** Network trips for document validation and embedding generation create massive CI/CD and production bottlenecks.
- **Orchestration Hell:** Managing cryptographic certificates (PKCS12) alongside AI data pipelines usually results in unmaintainable spaghetti code.

## ⚡ The 1-Minute Install
Zero-config deployment. Self-hosted by default. Tested on Linux and Windows (WSL2).

```bash
git clone https://github.com/franamaro-dev/VeriStack.git
cd VeriStack

# Spin up FastAPI, Qdrant (Vector DB), and n8n via Docker
docker compose up -d

# Check node health
curl http://localhost:8000/health
```

## 🧠 Key Features
*   🔒 **Privacy-first RAG:** 100% local embedding generation and document processing. External networks are bypassed by design.
*   🚀 **Async-First Core:** Built on FastAPI/Uvicorn for concurrent, non-blocking asynchronous certificate validation.
*   🇪🇸 **Drop-in Compliance:** Pre-configured endpoints for VeriFactu and TicketBAI `.p12`/`.pfx` node validation.
*   🧩 **Seamless Orchestration:** Ships with an isolated n8n container to visually route your compliance workflows over the internal bridge network.

## 🏗️ Architecture Stack
*   **API Gateway & Compute:** Python 3.11, FastAPI, Pydantic (V2)
*   **Vector Search & AI:** Qdrant (Local), Langchain Core
*   **Cryptography:** PyCA Cryptography (PKCS12, X.509)
*   **Workflows:** n8n (Locally hosted)

---
<div align="center">
  <i>Engineered for Senior-Level system architectures. Perfect for <b>FinTech</b> and <b>Enterprise</b> scale.</i>
</div>

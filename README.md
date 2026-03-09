<div align="center">
  <img src="https://raw.githubusercontent.com/franamaro-dev/VeriStack/main/.assets/header.jpg" width="100%" alt="VeriStack Banner">
</div>

# VeriStack

> **Arquitectura RAG Zero-trust para estricto cumplimiento financiero.**

VeriStack proporciona un backend self-hosted y async-first para validar certificados PKCS12 y procesar documentos financieros (TicketBAI / VeriFactu) mediante embeddings vectoriales locales. Cero fuga de datos. Latencia sub-second.

## ⚠️ El Problema
Construir pipelines financieros basados en IA expone vulnerabilidades críticas:
- **Violación de Soberanía del Dato:** Enviar facturas a APIs de terceros (OpenAI, Anthropic) rompe el estricto cumplimiento normativo europeo.
- **Overhead de Latencia:** Los viajes de red para validar documentos y generar embeddings crean cuellos de botella masivos en CI/CD y producción.
- **Infierno de Orquestación:** Gestionar certificados criptográficos (PKCS12) junto con pipelines de IA suele terminar en código espagueti inmanejable.

## ⚡ Instalación en 1 Minuto
Despliegue *Zero-config*. Self-hosted por defecto. Probado en Linux y Windows (WSL2).

```bash
git clone https://github.com/franamaro-dev/VeriStack.git
cd VeriStack

# Spin up FastAPI, Qdrant (Vector DB), and n8n via Docker
docker compose up -d

# Check node health
curl http://localhost:8000/health
```

## 🧠 Key Features
*   🔒 **Privacy-first RAG:** Generación de embeddings y procesamiento de documentos 100% local. Las redes externas se saltan por diseño.
*   🚀 **Async-First Core:** Construido sobre FastAPI/Uvicorn para validación concurrente asíncrona de certificados.
*   🇪🇸 **Drop-in Compliance:** Endpoints preconfigurados para validación de nodos `.p12`/`.pfx` de VeriFactu y TicketBAI.
*   🧩 **Orquestación Transparente:** Incluye un contenedor n8n aislado para enrutar visualmente tus flujos a través de redes bridge internas.

## 🏗️ Architecture Stack
*   **API Gateway & Compute:** Python 3.11, FastAPI, Pydantic (V2)
*   **Vector Search & AI:** Qdrant (Local), Langchain Core
*   **Criptografía:** PyCA Cryptography (PKCS12, X.509)
*   **Workflows:** n8n (Locally hosted)

---
<div align="center">
  <i>Ingeniería para arquitecturas de nivel Senior. Perfecto para escala <b>FinTech</b> y <b>Enterprise</b>.</i>
</div>

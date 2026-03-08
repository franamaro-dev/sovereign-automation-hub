# 🧪 Protocolo de Pruebas Técnicas

Este documento detalla cómo validar la integridad de la arquitectura soberana de forma local.

## 1. Verificación de Endpoints
Para comprobar que el microservicio responde correctamente, se deben ejecutar los siguientes comandos desde una terminal una vez levantado el stack con Docker:

### A. Health Check (Estado del Sistema)
```bash
curl -X GET http://localhost:8000/health

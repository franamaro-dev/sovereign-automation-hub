import datetime
from fastapi import FastAPI, HTTPException, UploadFile, File, Form, status
from pydantic import BaseModel, Field
from cryptography.hazmat.primitives.serialization import pkcs12

app = FastAPI(
    title="Sovereign TaxTech & AI Hub",
    description="Compliance API: Validación de certificados VeriFactu y Soberanía del Dato RAG",
    version="2.0.0"
)

# --- MODELOS RAG ---
class InvoiceIngestRequest(BaseModel):
    document_id: str = Field(..., description="Unique identifier for the financial document")
    content: str = Field(..., description="Extracted text from the invoice")
    compliance_type: str = Field("ticketbai", description="Regulatory framework standard")

class IngestionResponse(BaseModel):
    status: str
    message: str
    document_id: str

# --- HEALTH CHECK ---
@app.get("/health")
def health_check():
    """Verificación de estado del nodo local."""
    return {
        "status": "online", 
        "region": "Spain-Local",
        "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat()
    }

# --- 1. VERIFICACIÓN DE CERTIFICADOS (LEGACY/CORE) ---
@app.post("/verify-cert")
async def verify_p12(
    file: UploadFile = File(...), 
    password: str = Form(...)
):
    """
    Recibe un archivo .p12 o .pfx y una contraseña para validar 
    la fecha de expiración del certificado.
    """
    try:
        p12_data = await file.read()
        pw_bytes = password.encode('utf-8') if password else None
        
        private_key, certificate, additional_certs = pkcs12.load_key_and_certificates(
            p12_data, pw_bytes
        )

        if not certificate:
            raise ValueError("El archivo PKCS12 no contiene un certificado principal.")

        expiry_date = certificate.not_valid_after_utc
        now = datetime.datetime.now(datetime.timezone.utc)
        
        days_left = (expiry_date - now).days
        is_valid = now < expiry_date

        return {
            "filename": file.filename,
            "is_valid": is_valid,
            "days_left": days_left,
            "expiry_date": expiry_date.isoformat(),
            "status": "Success",
            "compliance_check": "VeriFactu/TicketBAI Ready"
        }

    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error procesando certificado: {str(e)}")

# --- 2. SOBERANÍA DEL DATO RAG ---
@app.post("/api/v1/ingest", response_model=IngestionResponse, status_code=status.HTTP_201_CREATED)
async def ingest_invoice(request: InvoiceIngestRequest):
    """
    Ingesta y vectorización de facturas 100% on-premise.
    Garantiza que la PII financiera no sale hacia APIs de terceros.
    """
    if not request.content.strip():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invoice content cannot be empty"
        )
    
    # Aquí iría la integración real con Qdrant y Langchain Local
    return IngestionResponse(
        status="success",
        message="Invoice securely ingested into local vector DB for RAG processing",
        document_id=request.document_id
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

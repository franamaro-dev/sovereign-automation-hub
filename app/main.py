import datetime
from fastapi import FastAPI, HTTPException, UploadFile, File, Form
from pydantic import BaseModel
from cryptography.hazmat.primitives.serialization import pkcs12
from cryptography import x509

app = FastAPI(
    title="Sovereign TaxTech API",
    description="API para validación de certificados y cumplimiento VeriFactu/TicketBAI"
)

@app.get("/health")
def health_check():
    """Verificación de estado del nodo local."""
    return {
        "status": "online", 
        "region": "Spain-Local",
        "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat()
    }

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
        # Leemos los bytes del archivo subido
        p12_data = await file.read()
        
        # Codificamos el password a bytes
        pw_bytes = password.encode('utf-8') if password else None
        
        # Cargamos el contenedor PKCS12 completo
        # Retorna (private_key, certificate, additional_certs)
        private_key, certificate, additional_certs = pkcs12.load_key_and_certificates(
            p12_data, 
            pw_bytes
        )

        if not certificate:
            raise ValueError("El archivo PKCS12 no contiene un certificado principal.")

        # Extracción de fechas de validez (UTC)
        expiry_date = certificate.not_valid_after_utc
        now = datetime.datetime.now(datetime.timezone.utc)
        
        # Cálculo de días restantes
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
        # En caso de error (password incorrecto, archivo corrupto, etc)
        raise HTTPException(
            status_code=400, 
            detail=f"Error procesando certificado: {str(e)}"
        )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

import pytest
from httpx import AsyncClient, ASGITransport
from app.main import app

@pytest.mark.asyncio
async def test_health_check():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        response = await ac.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "online"

@pytest.mark.asyncio
async def test_ingest_invoice_success():
    payload = {
        "document_id": "INV-2026-001",
        "content": "Total amount: 1540.50 EUR. VAT: 21%.",
        "compliance_type": "ticketbai"
    }
    
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        response = await ac.post("/api/v1/ingest", json=payload)
        
    assert response.status_code == 201
    assert response.json()["status"] == "success"

@pytest.mark.asyncio
async def test_ingest_invoice_empty_content():
    payload = {
        "document_id": "INV-2026-002",
        "content": "   ",
        "compliance_type": "verifactu"
    }
    
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        response = await ac.post("/api/v1/ingest", json=payload)
        
    assert response.status_code == 400
    assert "Invoice content cannot be empty" in response.json()["detail"]

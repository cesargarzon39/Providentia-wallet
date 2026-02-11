from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(title="Providentia Health Wallet API", version="0.1.0")

class FHIRPatient(BaseModel):
    resourceType: str = "Patient"
    id: Optional[str]
    active: bool = True
    name: List[dict]
    gender: str
    birthDate: str

@app.get("/")
async def root():
    return {"message": "Welcome to Providentia Health Wallet - Patient Centric Data"}

@app.post("/fhir/Patient")
async def create_patient(patient: FHIRPatient):
    # En el futuro, esto se guardará en PostgreSQL + JSONB
    return {"status": "received", "resource": patient}

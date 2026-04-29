"""FastAPI backend for GetFarm POC."""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.getfarm.core.risk import calculate_risk

app = FastAPI(title="GetFarm API", description="Pre-planting risk assessment")

class RiskRequest(BaseModel):
    region: str
    soil_moisture: float = None
    forecast_rainfall: float = None

class RiskResponse(BaseModel):
    status: str
    risk_score: float
    recommendation: str
    confidence: float

@app.get("/")
async def root():
    return {"message": "GetFarm API is running", "endpoints": ["/risk", "/health"]}

@app.post("/risk", response_model=RiskResponse)
async def risk_assessment(request: RiskRequest):
    """Calculate planting risk for a given region."""
    # Placeholder: In production, fetch real data by region
    # For POC, use defaults or passed values
    soil_moisture = request.soil_moisture or 35.0
    forecast_rainfall = request.forecast_rainfall or 45.0
    historical_avg = 50.0  # Placeholder
    
    result = calculate_risk(soil_moisture, forecast_rainfall, historical_avg)
    return RiskResponse(**result)

@app.get("/health")
async def health():
    return {"status": "healthy"}
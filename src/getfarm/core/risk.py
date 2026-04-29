"""Pre-planting risk assessment logic."""

def calculate_risk(soil_moisture: float, forecast_rainfall: float, historical_avg: float) -> dict:
    """
    Calculate planting risk based on soil moisture, forecast, and historical data.
    
    Returns:
        dict with keys: status (green/yellow/red), confidence, recommendation
    """
    # Combine factors into a risk score (0-100)
    risk_score = 0
    
    # Factor 1: Soil moisture (higher is better)
    if soil_moisture < 20:
        risk_score += 40
    elif soil_moisture < 40:
        risk_score += 20
    else:
        risk_score += 0
    
    # Factor 2: Forecast rainfall (higher is better)
    if forecast_rainfall < 30:
        risk_score += 40
    elif forecast_rainfall < 60:
        risk_score += 20
    else:
        risk_score += 0
    
    # Factor 3: Comparison to historical average
    if forecast_rainfall < historical_avg * 0.6:
        risk_score += 20
    elif forecast_rainfall < historical_avg * 0.8:
        risk_score += 10
    else:
        risk_score += 0
    
    # Determine status
    if risk_score < 30:
        status = "green"
        recommendation = "PLANT - Conditions are favorable"
    elif risk_score < 60:
        status = "yellow"
        recommendation = "DELAY - Consider waiting 2-3 weeks"
    else:
        status = "red"
        recommendation = "DO NOT PLANT - High risk of crop failure"
    
    return {
        "status": status,
        "risk_score": risk_score,
        "recommendation": recommendation,
        "confidence": 85  # Placeholder, would be model confidence
    }
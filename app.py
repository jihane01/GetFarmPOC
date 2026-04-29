"""Gradio frontend for GetFarm POC."""

import gradio as gr
import requests
import os

API_URL = os.getenv("API_URL", "http://localhost:8000")

def get_risk(region: str, soil_moisture: float, forecast_rainfall: float):
    """Call FastAPI backend and return formatted result."""
    try:
        response = requests.post(
            f"{API_URL}/risk",
            json={
                "region": region,
                "soil_moisture": soil_moisture,
                "forecast_rainfall": forecast_rainfall
            }
        )
        if response.status_code == 200:
            data = response.json()
            status_emoji = "🟢" if data["status"] == "green" else "🟡" if data["status"] == "yellow" else "🔴"
            return f"""
### {status_emoji} Risk Assessment for {region}

**Status:** {data["status"].upper()}
**Risk Score:** {data["risk_score"]}/100
**Recommendation:** {data["recommendation"]}
**Confidence:** {data["confidence"]}%
"""
        else:
            return f"Error: {response.status_code}"
    except Exception as e:
        return f"Connection error: {e}. Make sure API is running."

# Gradio interface
with gr.Blocks(title="GetFarm", theme=gr.themes.Soft()) as demo:
    gr.Markdown("""
    # 🌱 GetFarm: Pre-Planting Risk Assessment
    
    **Should you plant this season?** Enter your region and conditions below.
    """)
    
    with gr.Row():
        with gr.Column():
            region = gr.Textbox(label="Region", placeholder="e.g., Settat, Taliouine", value="Settat")
            soil_moisture = gr.Slider(0, 100, value=35, label="Soil Moisture (%)", step=5)
            forecast_rainfall = gr.Slider(0, 200, value=45, label="Forecast Rainfall (mm next 30 days)", step=5)
            submit_btn = gr.Button("Assess Risk", variant="primary")
        
        with gr.Column():
            output = gr.Markdown("Risk assessment will appear here")
    
    submit_btn.click(
        get_risk,
        inputs=[region, soil_moisture, forecast_rainfall],
        outputs=output
    )
    
    gr.Markdown("---\n**GetFarm** | AI for Moroccan farmers | [GitHub](https://github.com/jihane01/GetFarmPOC)")

if __name__ == "__main__":
    demo.launch(share=True)
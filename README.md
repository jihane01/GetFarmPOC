# GetFarm: Pre-Planting Risk Assessment for Moroccan Farmers

[![Python](https://img.shields.io/badge/python-3.9+-blue.svg)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104-green.svg)](https://fastapi.tiangolo.com)
[![Gradio](https://img.shields.io/badge/Gradio-4.8-orange.svg)](https://gradio.app)

## Problem

Moroccan farmers lose 5,000-10,000 MAD when they plant in drought years. No tool answers: *"Should I plant this season?"*

## Solution

GetFarm uses satellite data and weather forecasts to generate a risk score:
- 🟢 **Green**: Plant now
- 🟡 **Yellow**: Delay planting
- 🔴 **Red**: Do not plant

## Live Demo

[Deploy to Hugging Face Spaces here]

## Tech Stack

- **Backend**: FastAPI (Python)
- **Frontend**: Gradio
- **Package Manager**: uv
- **Deployment**: Hugging Face Spaces

## Run Locally

```bash
# Clone repo
git clone https://github.com/jihane01/GetFarmPOC.git
cd GetFarmPOC

# Install uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install dependencies
uv sync

# Run API (terminal 1)
uv run getfarm-api

# Run Gradio app (terminal 2)
uv run getfarm-app
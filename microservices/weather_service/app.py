from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI(title="Weather API Service", version="0.1.0")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

# Simple stubbed response. Configure REAL_WEATHER_API env var to proxy to a real provider.
REAL_PROVIDER = os.getenv("REAL_WEATHER_API")

@app.get("/health")
async def health():
    return {"status":"ok","service":"weather-api"}

@app.get("/weather")
async def get_weather(city: str = Query(..., description="City name")):
    # If REAL_PROVIDER is set, you could forward request (not implemented)
    sample = {
        "city": city,
        "temperature_c": 22.5,
        "condition": "Partly Cloudy",
        "source": "stub"
    }
    return sample

from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Analytics Service", version="0.1.0")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

class Event(BaseModel):
    user: str
    event: str
    meta: dict = {}

_events = []

@app.post('/track')
async def track(event: Event):
    _events.append(event.dict())
    return {"status":"ok"}

@app.get('/events')
async def events():
    return _events

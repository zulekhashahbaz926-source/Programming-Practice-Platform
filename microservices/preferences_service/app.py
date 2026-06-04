from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Preferences Service", version="0.1.0")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

class Pref(BaseModel):
    user: str
    prefs: dict

_store = {}

@app.post('/set')
async def set_pref(p: Pref):
    _store[p.user] = p.prefs
    return {"status":"saved"}

@app.get('/get')
async def get_pref(user: str):
    return _store.get(user, {})

from fastapi import FastAPI, BackgroundTasks
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Notification Service", version="0.1.0")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

class Notification(BaseModel):
    user: str
    channel: str
    message: str

_inbox = []

@app.post("/notify")
async def notify(payload: Notification, background: BackgroundTasks):
    _inbox.append(payload.dict())
    # placeholder for sending via email/push
    def send_stub(item):
        print("Sending notification:", item)
    background.add_task(send_stub, payload.dict())
    return {"status":"queued"}

@app.get("/inbox")
async def inbox():
    return _inbox

Microservice modules for Weather Dashboard

Each microservice is a minimal FastAPI app located in `microservices/`:

- `weather_service/app.py` — Weather API (stubbed)
- `notification_service/app.py` — Notification queue (stub)
- `analytics_service/app.py` — Analytics event collector (stub)
- `preferences_service/app.py` — User preference store (in-memory)

To run a service (example for weather):

```powershell
pip install fastapi uvicorn
uvicorn microservices.weather_service.app:app --reload --port 8100
```

Notes:
- The services are intentionally lightweight stubs to integrate with the desktop app.
- For production, add persistence, auth, and proper provider integrations.

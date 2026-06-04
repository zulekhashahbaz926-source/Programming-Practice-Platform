# Zyntriva Microservice

This module demonstrates a simple microservice for the Zyntriva project using FastAPI.

## Purpose
- Provide a separate API endpoint for learning module data and commit history.
- Demonstrate a microservice architecture component alongside the desktop application.
- Enable integration with external dashboards, web clients, or CI/CD tools.

## Endpoints
- `GET /health` — health check for the service
- `GET /modules` — list learning modules seeded in the database
- `GET /commits` — return commit history records
- `GET /users/{username}` — return profile details for a named user

## Run locally

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the service:

```bash
uvicorn microservice.app:app --reload --port 8000
```

Then open:

- http://127.0.0.1:8000/health
- http://127.0.0.1:8000/modules
- http://127.0.0.1:8000/commits
- http://127.0.0.1:8000/docs

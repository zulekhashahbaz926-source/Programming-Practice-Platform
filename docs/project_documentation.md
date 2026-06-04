# Zyntriva CodeForge — Project Documentation

## Overview
Zyntriva CodeForge is a Python desktop application built with CustomTkinter that simulates a programming-practice platform. It includes modules for problems, quizzes, peer review, testing, refactoring labs, and a small FastAPI microservice suite.

## Contents of this documentation
- Project purpose and scope
- Architecture overview
- Microservices and endpoints
- How to run the application and services
- How to generate UML diagrams and presentation slides

## Architecture
The desktop application uses an MVC-like pattern:

- UI: built with CustomTkinter (`core/app.py`, `dashboard/*`, `auth/*`)
- Controllers: coordinate UI actions and service calls
- Database: SQLite managed by `database/db_manager.py`
- Microservices: lightweight FastAPI services placed under `microservices/`

Recommended deployment: package desktop app with PyInstaller. Microservices can run independently (see `microservices/` folder).

## Microservices (stubs included)
- Weather API Service — `microservices/weather_service/app.py`
  - `GET /health` — health check
  - `GET /weather?city=...` — returns a stubbed weather payload

- Notification Service — `microservices/notification_service/app.py`
  - `POST /notify` — queue notification
  - `GET /inbox` — view queued notifications

- Analytics Service — `microservices/analytics_service/app.py`
  - `POST /track` — record an event
  - `GET /events` — list recorded events

- User Preferences Service — `microservices/preferences_service/app.py`
  - `POST /set` — set user prefs
  - `GET /get?user=...` — get user prefs

## Running locally
1. Install Python 3.11+ and dependencies from `requirements.txt`.

2. Run desktop app:

```powershell
pip install -r requirements.txt
python main.py
```

3. Run a microservice example (weather):

```powershell
pip install fastapi uvicorn
uvicorn microservices.weather_service.app:app --reload --port 8100
```

## UML diagrams
UML diagram sources were previously maintained in `docs/uml/`. If you need new diagrams, regenerate them with the scripts in `scripts/` (if present) or create Mermaid/SVG sources and place them into `docs/uml/`.

## Presentation
A PPTX generator script `scripts/create_presentation.py` creates a project presentation at `docs/project_presentation.pptx`. It will include text slides and any available images from `docs/uml/` if present.

## Deliverables
- Source code (this repository)
- Microservice stubs in `microservices/`
- Presentation: `docs/project_presentation.pptx` (generated)
- Guidance to regenerate diagrams and presentations (see this file)

## Support
Tell me which slides or diagrams you want in the presentation, or if you want me to regenerate UML diagrams from scratch (Mermaid or SVG). I can also push the presentation to GitHub for download.

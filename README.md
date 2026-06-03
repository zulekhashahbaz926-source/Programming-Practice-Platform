# Zyntriva CodeForge – Programming Practices Platform

Zyntriva CodeForge is a professional desktop application built with Python and CustomTkinter for university-level software engineering education. The platform demonstrates modern software construction practices with a dark futuristic UI, modular architecture, SQLite integration, and a full authentication workflow.

## Features

- Professional authentication with login and registration
- Modular dashboard with sidebar navigation and interactive cards
- Process model learning, version control simulator, refactoring lab, testing module, exception handling lab, peer review tools, deployment overview, and team management
- SQLite data persistence
- Theme switcher, notifications, activity logs, and search bar
- Logging and exception handling
- Unit tests for authentication, database, and validation logic

## Technology

- Python 3.x
- CustomTkinter (modern UI)
- SQLite
- OOP and modular design
- MVC-like structure

## Setup

1. Install Python 3.11 or newer.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the application:

```bash
python main.py
```

## Project Structure

 - `docs/` — report outline and academic deliverables (UML diagrams now in `docs/uml/`)
 - `microservice/` — FastAPI microservice exposing module and commit data
 - `microservices/` — suggested microservices for Weather Dashboard (stubs in `microservices/`)

## Testing

Run unit tests with:

```bash
python -m unittest discover tests
```

## Academic Project Requirements

This project includes the following software construction concepts:

* Process model selection and justification (Agile-inspired iterative development)
* Software process improvement (SPI) via refactoring, test expansion, and content updates
* Version control simulation with commit history and branch concepts
* Lehman’s Law illustration through continuous application evolution and feature growth
* Deployment planning for packaging the desktop application with PyInstaller
* Legacy code refactoring and modular architecture
* Unit testing and automated validation via `unittest`
* Exception handling through custom exceptions and logged error handling
* Peer review support with inspection checklists and review records

## Report + Presentation Guidance

For the final semester deliverable, include these sections in the report:

1. Chosen process model and justification
2. Software process improvement activities performed
3. Version control implementation and commit tracking
4. Lehman’s Law evidence from the application lifecycle
5. Deployment approach and packaging strategy
6. Refactoring actions applied to the codebase
7. Unit test coverage and automated testing setup
8. Exception handling design and error management
9. Peer review process and team contribution tracking
10. Team roles, contributions, and learning outcomes

# Project Report

## Introduction
The **Programming Practices Platform** is a desktop application built for students to practice programming through exercises and challenges. The project follows a clean, three‑layer architecture (UI → Service → Repository) and adheres to OOP principles, making it highly maintainable and testable.

## Architecture Overview
- **UI Layer** (`src/ui/`): Implemented with **CustomTkinter**, provides a modern sidebar navigation, dashboard cards, exercise editor, and settings panel. All UI components are stateless wrappers that delegate work to service classes.
- **Service Layer** (`src/core/`): Contains business logic:
  - `AuthService` – registration and login with bcrypt.
  - `ExerciseManager` – load exercises, evaluate submissions.
  - `ChallengeManager` – generate difficulty‑based challenges, track attempts, score weighting.
  - `ProgressTracker` – record and compute progress statistics.
- **Repository Layer** (`src/db/repositories.py`): Encapsulates all SQLite CRUD operations via a lightweight `Database` context manager. No direct SQL is performed outside these classes.
- **Models** (`src/db/models.py`): Dataclasses representing domain entities (`User`, `Exercise`, `Progress`, `Challenge`).
- **Utilities** (`src/utils/`): Logging, configuration, custom exceptions.

## Design Decisions
| Decision | Rationale |
|----------|-----------|
| **CustomTkinter** for UI | Provides a modern look while staying pure Python (no external UI frameworks). |
| **SQLite** for persistence | Simple file‑based DB, no server needed, suitable for a desktop app. |
| **bcrypt** for passwords | Industry‑standard hashing with built‑in salt handling. |
| **Repository Pattern** | Guarantees separation of concerns, easier mocking in tests, and clear data‑access boundaries. |
| **Stateless Services** | Improves testability; each method receives needed data and returns results without hidden state. |
| **PyInstaller** packaging | Produces a single Windows executable for distribution, matching project constraints. |

## Testing Strategy
- **Pytest** is used as the test framework (added to `requirements.txt`).
- Fixtures create a temporary SQLite DB for each test, ensuring isolation.
- Tests cover:
  - Auth flow (registration, login, validation errors).
  - CRUD operations of all repositories.
  - Business logic of `ExerciseManager` and `ChallengeManager` (including difficulty validation and non‑repetition).
- Coverage target ≥ 80 %.

## UML Diagrams (generated with PlantUML)
- **Use Case Diagram** – shows actors (Student, System) and primary use cases (Register, Login, Solve Exercise, Attempt Challenge, View Dashboard, Change Settings).
- **Class Diagram** – visualizes relationships among `AuthService`, `ExerciseManager`, `ChallengeManager`, `ProgressTracker`, repository classes, and model dataclasses.
- **Sequence Diagram** – outlines the interaction for *Login → Dashboard → Exercise* flow.
- **Activity Diagram** – depicts the challenge solving process (select difficulty, generate challenge, submit solution, store result).
- **ER Diagram** – represents SQLite schema with tables `users`, `exercises`, `progress`, `challenges` and their foreign key relationships.

> The diagrams are stored in `docs/diagrams/` as both PNG and SVG files.

## Packaging (PyInstaller)
- **`pyinstaller.spec`** defines the entry point `src/ui/app.py`, includes the `assets/` folder, and sets the custom icon (`assets/icon.ico`).
- **`build_exe.bat`** runs `pyinstaller --clean pyinstaller.spec`.
- The resulting `.exe` creates the SQLite DB in the user’s home directory (`%USERPROFILE%\ProgrammingPracticesPlatform\data`).

## Future Work
- Add **leaderboards** and **multiplayer challenges**.
- Implement **daily challenge** scheduler.
- Extend **unit tests** for UI components using a headless test framework.
- CI/CD pipeline with GitHub Actions to run tests and build the executable on each push.

---
*Prepared for final submission as part of the FYP.*

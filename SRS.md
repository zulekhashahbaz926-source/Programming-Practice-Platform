# Software Requirements Specification (SRS)

## 1. Introduction
### 1.1 Purpose
The **Programming Practices Platform** is a desktop application that provides students with coding exercises, challenges, and progress tracking to improve programming skills.
### 1.2 Scope
The system supports user authentication, exercise management, challenge generation, progress analytics, and a modern UI built with CustomTkinter. It runs on Windows and stores data locally using SQLite.
### 1.3 Definitions, Acronyms, Abbreviations
- **UI** – User Interface
- **CRUD** – Create, Read, Update, Delete
- **FYP** – Final Year Project
### 1.4 Overview
The document describes functional and non‑functional requirements, interface specifications, and design constraints.

## 2. Overall Description
### 2.1 Product Perspective
Standalone desktop application, no external services required.
### 2.2 Product Functions
- Register / Login with bcrypt‑hashed passwords.
- Dashboard showing completed exercises, total score, accuracy.
- Exercise view with code editor and automatic feedback.
- Random challenge generation with difficulty levels.
- Persistent storage of users, exercises, progress, and challenges.
- Theme toggle (dark/light) and settings panel.
### 2.3 User Characteristics
Students with basic computer literacy; no special training required.
### 2.4 Constraints
- Windows‑only build (PyInstaller).
- All database access through repository layer.
- UI must use only CustomTkinter components.
### 2.5 Assumptions and Dependencies
- Python 3.11+ installed.
- Required packages listed in `requirements.txt`.

## 3. Specific Requirements
### 3.1 Functional Requirements
1. **Authentication**
   - FR1.1: Users can register with a unique username, strong password, and optional email.
   - FR1.2: Passwords are stored as bcrypt hashes.
   - FR1.3: Users can log in with correct credentials.
2. **Exercise Management**
   - FR2.1: List exercises by category.
   - FR2.2: Evaluate user code against stored solution and provide feedback.
3. **Challenge Management**
   - FR3.1: Generate a random challenge based on selected difficulty.
   - FR3.2: Track attempts and assign weighted scores.
4. **Progress Tracking**
   - FR4.1: Record each exercise completion with score.
   - FR4.2: Compute completion rate and average score.
5. **UI Navigation**
   - FR5.1: Sidebar navigation between Dashboard, Exercises, Challenges, Settings.
   - FR5.2: Theme can be toggled and persisted.
### 3.2 Non‑Functional Requirements
- **Performance**: UI response < 200 ms for navigation.
- **Usability**: Consistent modern design, accessible fonts.
- **Reliability**: No crashes; data persisted across sessions.
- **Maintainability**: Clean modular code, OOP principles, test coverage ≥ 80%.
- **Portability**: Packaged as a single Windows .exe.

## 4. External Interface Requirements
### 4.1 User Interfaces
- CustomTkinter windows and widgets as described in UI design.
### 4.2 Software Interfaces
- Python standard library, `customtkinter`, `bcrypt`, `sqlite3`.
### 4.3 Hardware Interfaces
- No special hardware; runs on any Windows PC.

## 5. System Architecture
- Three‑layer architecture: UI → Service (AuthService, ExerciseManager, ChallengeManager, ProgressTracker) → Repository (SQLite via Database wrapper).
- All services are stateless and injected with repository instances for testability.

## 6. Appendices
- Glossary, Acronyms, References.

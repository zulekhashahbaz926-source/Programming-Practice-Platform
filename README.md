<<<<<<< HEAD
# Programming Practices Platform

## Overview
A modern desktop application built with **Python**, **CustomTkinter**, and **SQLite** that helps students improve coding skills through exercises, challenges, and progress tracking.

## Features
- User authentication (bcrypt‑hashed passwords)
- Dashboard with progress overview cards
- Exercise view with code editor, real‑time feedback
- Random coding challenges with difficulty levels
- Persistent storage of users, exercises, progress, and challenges
- Theme‑aware UI (dark/light) using CustomTkinter
- Unit tests with **pytest**
- Cross‑platform packaging for Windows via **PyInstaller**

## Installation
```bash
# Clone the repository
git clone <repo_url>
cd ProgrammingPracticesPlatform

# Create a virtual environment (recommended)
python -m venv venv
venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt
```

## Usage
```bash
# Run the application
python src/ui/app.py
```

## Development
- Run tests: `pytest`
- Add new exercises via `src/db/repositories.ExerciseRepository`
- Extend UI by editing files in `src/ui/`

## License
MIT License
=======
# Programming-Practice-Platform
A Python-based desktop Programming Practice Platform that allows users to practice coding problems, take quizzes, and track progress. It includes a built-in code editor, multiple difficulty levels, and instant result evaluation to help beginners learn programming through interactive practice and performance tracking.
>>>>>>> eb38cb3155a89a65ce3d78b6f0ebdde221b2dc5a

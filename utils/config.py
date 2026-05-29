# utils/config.py
"""Configuration module for the Programming Practices Platform.
Contains constants such as database path, logging settings, and UI defaults.
"""

import os
from pathlib import Path

# Base directory of the project (assumes this file is located in utils/)
BASE_DIR = Path(__file__).resolve().parent.parent

# Path to the SQLite database file (created on first run)
DB_PATH = BASE_DIR / "database" / "app.db"

# Logging configuration
LOG_DIR = BASE_DIR / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)
LOG_FILE = LOG_DIR / "app.log"

# UI defaults
WINDOW_TITLE = "Programming Practices Platform"
WINDOW_SIZE = "1024x768"
THEME = "darkly"  # ttkbootstrap theme name

import logging
import os
from logging.handlers import RotatingFileHandler

LOG_DIR = os.path.join(os.path.dirname(__file__), "..", "..", "logs")
os.makedirs(LOG_DIR, exist_ok=True)
LOG_FILE = os.path.join(LOG_DIR, "app.log")

def setup_logging(level: int = logging.INFO):
    """Configure a rotating file logger for the application.
    Logs are written to `logs/app.log` with a max size of 5MB and 3 backups.
    """
    logger = logging.getLogger()
    logger.setLevel(level)
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    handler = RotatingFileHandler(LOG_FILE, maxBytes=5 * 1024 * 1024, backupCount=3)
    handler.setFormatter(formatter)
    logger.addHandler(handler)

def get_logger(name: str) -> logging.Logger:
    """Convenient helper to obtain a module‑specific logger."""
    return logging.getLogger(name)

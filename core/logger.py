import logging
from logging.handlers import RotatingFileHandler
from config.settings import LOG_FILE

LOG_FORMAT = "%(asctime)s %(levelname)s %(name)s %(message)s"

def create_logger(name: str):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    if not logger.handlers:
        handler = RotatingFileHandler(LOG_FILE, maxBytes=1024 * 1024, backupCount=3, encoding="utf-8")
        handler.setFormatter(logging.Formatter(LOG_FORMAT))
        logger.addHandler(handler)
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(logging.Formatter("%(levelname)s: %(message)s"))
        logger.addHandler(console_handler)
    return logger

app_logger = create_logger("Zyntriva")

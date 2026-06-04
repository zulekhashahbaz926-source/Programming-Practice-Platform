import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
APP_NAME = "Zyntriva CodeForge"
APP_VERSION = "v3.4.0"
DB_PATH = os.path.join(BASE_DIR, "zyntriva_codeforge.db")
LOG_FILE = os.path.join(BASE_DIR, "logs", "app.log")
DEFAULT_THEME = "dark"
VERSION = "1.0.0"

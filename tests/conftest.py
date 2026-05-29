import os
import sys
import tempfile
import pytest

# Ensure the src package is importable
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from src.db.database import Database

@pytest.fixture(scope='function')
def temp_db_path():
    """Create a temporary SQLite database file and return its path.
    The Database class will initialize required tables on first use.
    """
    fd, path = tempfile.mkstemp(suffix='.db')
    os.close(fd)
    # Initialize tables via Database context manager (creates file if not exists)
    with Database(path) as db:
        pass  # tables are created in repository init
    yield path
    # Cleanup
    try:
        os.remove(path)
    except OSError:
        pass

@pytest.fixture(scope='function')
def db(temp_db_path):
    """Provide a Database instance bound to the temporary path."""
    return Database(temp_db_path)

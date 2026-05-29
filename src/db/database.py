import sqlite3
from pathlib import Path

class Database:
    """Simple SQLite wrapper handling connection and cursor lifecycle."""

    def __init__(self, db_path: str | Path = "programming_practices.db"):
        self.db_path = Path(db_path)
        self.connection: sqlite3.Connection | None = None
        self._ensure_db_directory()

    def _ensure_db_directory(self) -> None:
        """Create parent directory for the database file if it does not exist."""
        if not self.db_path.parent.exists():
            self.db_path.parent.mkdir(parents=True, exist_ok=True)

    def connect(self) -> None:
        """Open a connection to the SQLite database."""
        self.connection = sqlite3.connect(self.db_path)
        self.connection.row_factory = sqlite3.Row

    def close(self) -> None:
        """Close the SQLite connection if open."""
        if self.connection:
            self.connection.close()
            self.connection = None

    def execute(self, query: str, params: tuple = ()) -> sqlite3.Cursor:
        """Execute a query and return the cursor.

        Args:
            query: SQL statement.
            params: Parameters for parametrised queries.
        """
        if self.connection is None:
            raise RuntimeError("Database connection is not established. Call connect() first.")
        cursor = self.connection.cursor()
        cursor.execute(query, params)
        self.connection.commit()
        return cursor

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

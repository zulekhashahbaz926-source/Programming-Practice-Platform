import sqlite3
import os
from datetime import datetime
from typing import Any, Dict, List, Optional
from config.settings import DB_PATH
from core.logger import app_logger
from utils.exceptions import DatabaseError

class DatabaseManager:
    def __init__(self, db_path: Optional[str] = None):
        self.db_path = db_path or DB_PATH
        directory = os.path.dirname(self.db_path)
        if directory:
            os.makedirs(directory, exist_ok=True)
        self.conn = sqlite3.connect(self.db_path, check_same_thread=False)
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()

    def initialize_schema(self):
        try:
            self.cursor.executescript(
                """
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    full_name TEXT NOT NULL,
                    username TEXT UNIQUE NOT NULL,
                    email TEXT UNIQUE NOT NULL,
                    password TEXT NOT NULL,
                    created_at TEXT NOT NULL
                );
                CREATE TABLE IF NOT EXISTS quizzes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    description TEXT,
                    category TEXT,
                    content TEXT
                );
                CREATE TABLE IF NOT EXISTS commits (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    branch TEXT,
                    message TEXT,
                    author TEXT,
                    timestamp TEXT
                );
                CREATE TABLE IF NOT EXISTS reviews (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT,
                    status TEXT,
                    reviewer TEXT,
                    comments TEXT,
                    created_at TEXT
                );
                CREATE TABLE IF NOT EXISTS tests (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    status TEXT,
                    result TEXT,
                    description TEXT,
                    created_at TEXT
                );
                CREATE TABLE IF NOT EXISTS notifications (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT,
                    message TEXT,
                    user_id INTEGER,
                    created_at TEXT,
                    seen INTEGER DEFAULT 0
                );
                """
            )
            self.conn.commit()
        except Exception as exc:
            app_logger.exception("Failed to initialize database schema.")
            raise exc

    def execute(self, query: str, params: tuple = ()) -> sqlite3.Cursor:
        try:
            cur = self.cursor.execute(query, params)
            self.conn.commit()
            return cur
        except Exception as exc:
            app_logger.exception(f"Database execution failed: {query} {params}")
            raise DatabaseError(str(exc)) from exc

    def fetchone(self, query: str, params: tuple = ()) -> Optional[sqlite3.Row]:
        try:
            self.cursor.execute(query, params)
            return self.cursor.fetchone()
        except Exception as exc:
            app_logger.exception(f"Database fetchone failed: {query} {params}")
            raise DatabaseError(str(exc)) from exc

    def fetchall(self, query: str, params: tuple = ()) -> List[sqlite3.Row]:
        try:
            self.cursor.execute(query, params)
            return self.cursor.fetchall()
        except Exception as exc:
            app_logger.exception(f"Database fetchall failed: {query} {params}")
            raise DatabaseError(str(exc)) from exc

    def create_user(self, full_name: str, username: str, email: str, password: str) -> int:
        timestamp = datetime.now().isoformat()
        result = self.execute(
            "INSERT INTO users (full_name, username, email, password, created_at) VALUES (?, ?, ?, ?, ?)",
            (full_name, username, email, password, timestamp),
        )
        return result.lastrowid

    def find_user_by_email(self, email: str) -> Optional[sqlite3.Row]:
        return self.fetchone("SELECT * FROM users WHERE LOWER(email) = LOWER(?)", (email,))

    def find_user_by_username(self, username: str) -> Optional[sqlite3.Row]:
        return self.fetchone("SELECT * FROM users WHERE LOWER(username) = LOWER(?)", (username,))

    def get_notifications(self, user_id: int) -> List[sqlite3.Row]:
        return self.fetchall(
            "SELECT * FROM notifications WHERE user_id = ? ORDER BY created_at DESC LIMIT 5", (user_id,)
        )

    def get_recent_activity(self) -> List[sqlite3.Row]:
        return self.fetchall(
            "SELECT title, message, created_at FROM notifications ORDER BY created_at DESC LIMIT 6"
        )

    def get_stat_counts(self) -> Dict[str, int]:
        return {
            "commits": self.fetchone("SELECT COUNT(*) AS count FROM commits")["count"],
            "reviews": self.fetchone("SELECT COUNT(*) AS count FROM reviews")["count"],
            "tests": self.fetchone("SELECT COUNT(*) AS count FROM tests")["count"],
            "notifications": self.fetchone("SELECT COUNT(*) AS count FROM notifications")["count"],
        }

    def get_commits(self) -> List[sqlite3.Row]:
        return self.fetchall("SELECT * FROM commits ORDER BY id DESC LIMIT 6")

    def get_quizzes(self) -> List[sqlite3.Row]:
        return self.fetchall("SELECT * FROM quizzes ORDER BY id DESC LIMIT 5")

    def create_notification(self, title: str, message: str, user_id: int):
        timestamp = datetime.now().isoformat()
        self.execute(
            "INSERT INTO notifications (title, message, user_id, created_at) VALUES (?, ?, ?, ?)",
            (title, message, user_id, timestamp),
        )

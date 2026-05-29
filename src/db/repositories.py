import sqlite3
from pathlib import Path
from typing import List, Optional

from .database import Database
from .models import User, Exercise, Progress, Challenge

# --------------------- User Repository ---------------------
class UserRepository:
    """Repository handling User CRUD operations."""

    def __init__(self, db_path: str | Path = "programming_practices.db"):
        self.db_path = Path(db_path)
        self._init_table()

    def _init_table(self) -> None:
        with Database(self.db_path) as db:
            db.execute(
                """
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE NOT NULL,
                    password_hash TEXT NOT NULL,
                    created_at TEXT DEFAULT (datetime('now'))
                )
                """
            )

    def add_user(self, username: str, password_hash: str) -> User:
        with Database(self.db_path) as db:
            cursor = db.execute(
                "INSERT INTO users (username, password_hash) VALUES (?, ?)",
                (username, password_hash),
            )
            user_id = cursor.lastrowid
            return User(id=user_id, username=username, password_hash=password_hash)

    def get_user_by_username(self, username: str) -> Optional[User]:
        with Database(self.db_path) as db:
            cursor = db.execute(
                "SELECT id, username, password_hash FROM users WHERE username = ?",
                (username,),
            )
            row = cursor.fetchone()
            if row:
                return User(id=row["id"], username=row["username"], password_hash=row["password_hash"])
            return None

    def list_users(self) -> List[User]:
        with Database(self.db_path) as db:
            cursor = db.execute("SELECT id, username, password_hash FROM users")
            return [User(id=row["id"], username=row["username"], password_hash=row["password_hash"]) for row in cursor]

# --------------------- Exercise Repository ---------------------
class ExerciseRepository:
    """Repository for Exercise CRUD operations."""

    def __init__(self, db_path: str | Path = "programming_practices.db"):
        self.db_path = Path(db_path)
        self._init_table()

    def _init_table(self) -> None:
        with Database(self.db_path) as db:
            db.execute(
                """
                CREATE TABLE IF NOT EXISTS exercises (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    description TEXT,
                    solution TEXT,
                    category TEXT CHECK(category IN ('Beginner','Intermediate','Advanced'))
                )
                """
            )

    def add_exercise(self, title: str, description: str, solution: str, category: str = "Beginner") -> Exercise:
        with Database(self.db_path) as db:
            cursor = db.execute(
                "INSERT INTO exercises (title, description, solution, category) VALUES (?,?,?,?)",
                (title, description, solution, category),
            )
            ex_id = cursor.lastrowid
            return Exercise(id=ex_id, title=title, description=description, solution=solution, category=category)

    def get_exercise(self, exercise_id: int) -> Optional[Exercise]:
        with Database(self.db_path) as db:
            cursor = db.execute(
                "SELECT id, title, description, solution, category FROM exercises WHERE id = ?",
                (exercise_id,),
            )
            row = cursor.fetchone()
            if row:
                return Exercise(
                    id=row["id"],
                    title=row["title"],
                    description=row["description"],
                    solution=row["solution"],
                    category=row["category"],
                )
            return None

    def list_exercises(self) -> List[Exercise]:
        with Database(self.db_path) as db:
            cursor = db.execute("SELECT id, title, description, solution, category FROM exercises")
            return [
                Exercise(
                    id=row["id"],
                    title=row["title"],
                    description=row["description"],
                    solution=row["solution"],
                    category=row["category"],
                )
                for row in cursor
            ]

# --------------------- Progress Repository ---------------------
class ProgressRepository:
    """Repository to store user progress on exercises."""

    def __init__(self, db_path: str | Path = "programming_practices.db"):
        self.db_path = Path(db_path)
        self._init_table()

    def _init_table(self) -> None:
        with Database(self.db_path) as db:
            db.execute(
                """
                CREATE TABLE IF NOT EXISTS progress (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER NOT NULL,
                    exercise_id INTEGER NOT NULL,
                    completed INTEGER NOT NULL CHECK(completed IN (0,1)),
                    score REAL DEFAULT 0,
                    timestamp TEXT DEFAULT (datetime('now')),
                    FOREIGN KEY(user_id) REFERENCES users(id),
                    FOREIGN KEY(exercise_id) REFERENCES exercises(id)
                )
                """
            )

    def record_progress(
        self,
        user_id: int,
        exercise_id: int,
        completed: bool,
        score: float = 0.0,
    ) -> Progress:
        with Database(self.db_path) as db:
            cursor = db.execute(
                "INSERT INTO progress (user_id, exercise_id, completed, score) VALUES (?,?,?,?)",
                (user_id, exercise_id, int(completed), score),
            )
            prog_id = cursor.lastrowid
            return Progress(
                id=prog_id,
                user_id=user_id,
                exercise_id=exercise_id,
                completed=completed,
                score=score,
            )

    def get_user_progress(self, user_id: int) -> List[Progress]:
        with Database(self.db_path) as db:
            cursor = db.execute(
                "SELECT id, user_id, exercise_id, completed, score, timestamp FROM progress WHERE user_id = ?",
                (user_id,),
            )
            return [
                Progress(
                    id=row["id"],
                    user_id=row["user_id"],
                    exercise_id=row["exercise_id"],
                    completed=bool(row["completed"]),
                    score=row["score"],
                    timestamp=row["timestamp"],
                )
                for row in cursor
            ]

# --------------------- Challenge Repository ---------------------
class ChallengeRepository:
    """Repository for coding challenges."""

    def __init__(self, db_path: str | Path = "programming_practices.db"):
        self.db_path = Path(db_path)
        self._init_table()

    def _init_table(self) -> None:
        with Database(self.db_path) as db:
            db.execute(
                """
                CREATE TABLE IF NOT EXISTS challenges (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    description TEXT,
                    difficulty TEXT CHECK(difficulty IN ('Beginner','Intermediate','Advanced')),
                    solution TEXT,
                    created_at TEXT DEFAULT (datetime('now'))
                )
                """
            )

    def add_challenge(
        self,
        title: str,
        description: str,
        difficulty: str = "Beginner",
        solution: str = "",
    ) -> Challenge:
        with Database(self.db_path) as db:
            cursor = db.execute(
                "INSERT INTO challenges (title, description, difficulty, solution) VALUES (?,?,?,?)",
                (title, description, difficulty, solution),
            )
            ch_id = cursor.lastrowid
            return Challenge(
                id=ch_id,
                title=title,
                description=description,
                difficulty=difficulty,
                solution=solution,
            )

    def get_challenge(self, challenge_id: int) -> Optional[Challenge]:
        with Database(self.db_path) as db:
            cursor = db.execute(
                "SELECT id, title, description, difficulty, solution, created_at FROM challenges WHERE id = ?",
                (challenge_id,),
            )
            row = cursor.fetchone()
            if row:
                return Challenge(
                    id=row["id"],
                    title=row["title"],
                    description=row["description"],
                    difficulty=row["difficulty"],
                    solution=row["solution"],
                    created_at=row["created_at"],
                )
            return None

    def list_challenges(self) -> List[Challenge]:
        with Database(self.db_path) as db:
            cursor = db.execute(
                "SELECT id, title, description, difficulty, solution, created_at FROM challenges"
            )
            return [
                Challenge(
                    id=row["id"],
                    title=row["title"],
                    description=row["description"],
                    difficulty=row["difficulty"],
                    solution=row["solution"],
                    created_at=row["created_at"],
                )
                for row in cursor
            ]

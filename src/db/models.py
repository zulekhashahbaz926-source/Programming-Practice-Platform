from dataclasses import dataclass
from datetime import datetime

@dataclass
class User:
    id: int | None = None
    username: str = ""
    password_hash: str = ""
    created_at: datetime | None = None

@dataclass
class Exercise:
    id: int | None = None
    title: str = ""
    description: str = ""
    solution: str = ""
    category: str = "Beginner"  # Beginner / Intermediate / Advanced

@dataclass
class Progress:
    id: int | None = None
    user_id: int = 0
    exercise_id: int = 0
    completed: bool = False
    score: float = 0.0
    timestamp: datetime | None = None

@dataclass
class Setting:
    id: int | None = None
    user_id: int = 0
    key: str = ""
    value: str = ""

@dataclass
class Challenge:
    id: int | None = None
    title: str = ""
    description: str = ""
    difficulty: str = "Beginner"  # Beginner / Intermediate / Advanced
    solution: str = ""
    created_at: datetime | None = None

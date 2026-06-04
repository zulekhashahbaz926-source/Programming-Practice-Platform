import bcrypt
from typing import Dict, Optional
from core.logger import app_logger
from database.db_manager import DatabaseManager
from utils.validators import validate_email, validate_password, validate_username
from utils.exceptions import AuthenticationError, ValidationError

class AuthController:
    def __init__(self, db: DatabaseManager):
        self.db = db

    def _hash_password(self, password: str) -> str:
        raw_hash = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
        return raw_hash.decode("utf-8")

    def register_user(self, full_name: str, username: str, email: str, password: str, confirm_password: str) -> Dict[str, str]:
        if not full_name.strip():
            raise ValidationError("Full name is required.")
        if not validate_username(username):
            raise ValidationError("Username must be at least 4 characters and contain only letters or numbers.")
        if not validate_email(email):
            raise ValidationError("Please enter a valid email address.")
        if password != confirm_password:
            raise ValidationError("Passwords do not match.")
        if not validate_password(password):
            raise ValidationError("Password must be at least 8 characters.")
        if self.db.find_user_by_username(username):
            raise ValidationError("Username already exists.")
        if self.db.find_user_by_email(email):
            raise ValidationError("Email already registered.")

        password_hash = self._hash_password(password)
        self.db.create_user(full_name, username, email, password_hash)
        app_logger.info(f"New account created: {username}")
        return {"username": username, "email": email}

    def authenticate_user(self, username_or_email: str, password: str) -> Optional[Dict[str, str]]:
        if not username_or_email.strip() or not password:
            raise AuthenticationError("Please provide your username or email and password.")
        user = self.db.find_user_by_username(username_or_email)
        if not user:
            user = self.db.find_user_by_email(username_or_email)
        if not user:
            raise AuthenticationError("User not found.")
        if not bcrypt.checkpw(password.encode("utf-8"), user["password"].encode("utf-8")):
            raise AuthenticationError("Invalid password.")
        app_logger.info(f"Authenticated user: {user['username']}")
        return dict(user)

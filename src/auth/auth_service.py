"""Authentication service for the Programming Practices Platform.

Provides user registration and login functionality using bcrypt for secure password
hashing. The service delegates all database interactions to :class:`UserRepository`
and raises custom exceptions from :mod:`src.utils.exceptions` for error handling.
"""

import re
from typing import Optional

import bcrypt

from src.db.repositories import UserRepository
from src.db.models import User
from src.utils.exceptions import ValidationError, AuthenticationError


class AuthService:
    """Service layer handling user authentication.

    The class is deliberately stateless – it creates a new ``UserRepository``
    instance for each operation, which keeps the database logic isolated and
    makes the service easily testable (dependency injection can replace the
    repository in unit tests).
    """

    USERNAME_REGEX = re.compile(r"^[A-Za-z0-9_]{3,30}$")
    EMAIL_REGEX = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
    MIN_PASSWORD_LENGTH = 8

    def __init__(self, db_path: Optional[str] = None):
        """Create an :class:`AuthService`.

        Parameters
        ----------
        db_path: Optional[str]
            Path to the SQLite file. If ``None`` the default path used by
            :class:`UserRepository` (``programming_practices.db``) is applied.
        """
        self._user_repo = UserRepository(db_path) if db_path else UserRepository()

    # ---------------------------------------------------------------------
    # Public API
    # ---------------------------------------------------------------------
    def register(self, username: str, password: str, email: Optional[str] = None) -> User:
        """Register a new user.

        Performs validation, checks for duplicate usernames, hashes the password
        with ``bcrypt`` and stores the user via :class:`UserRepository`.

        Returns
        -------
        User
            The freshly created ``User`` dataclass instance.

        Raises
        ------
        ValidationError
            If any input does not satisfy the validation rules.
        AuthenticationError
            If a user with the given username already exists.
        """
        self._validate_username(username)
        if email is not None:
            self._validate_email(email)
        self._validate_password(password)

        if self._user_repo.get_user_by_username(username) is not None:
            raise AuthenticationError(f"Username '{username}' is already taken.")

        password_hash = self._hash_password(password)
        # Store the user – the repository returns a User instance with the ID set.
        user = self._user_repo.add_user(username=username, password_hash=password_hash)
        return user

    def login(self, username: str, password: str) -> User:
        """Authenticate a user.

        Parameters
        ----------
        username: str
            The username supplied at login.
        password: str
            Plain‑text password entered by the user.

        Returns
        -------
        User
            The authenticated user's data record.

        Raises
        ------
        AuthenticationError
            If the username does not exist or the password verification fails.
        """
        user = self._user_repo.get_user_by_username(username)
        if user is None:
            raise AuthenticationError("Invalid username or password.")

        if not self._verify_password(password, user.password_hash):
            raise AuthenticationError("Invalid username or password.")
        return user

    # ---------------------------------------------------------------------
    # Private helpers – validation and cryptography
    # ---------------------------------------------------------------------
    def _validate_username(self, username: str) -> None:
        if not username:
            raise ValidationError("Username cannot be empty.")
        if not self.USERNAME_REGEX.fullmatch(username):
            raise ValidationError(
                "Username must be 3‑30 characters long and contain only letters, numbers, or underscores."
            )

    def _validate_email(self, email: str) -> None:
        if not self.EMAIL_REGEX.fullmatch(email):
            raise ValidationError("Invalid email address format.")

    def _validate_password(self, password: str) -> None:
        if len(password) < self.MIN_PASSWORD_LENGTH:
            raise ValidationError(
                f"Password must be at least {self.MIN_PASSWORD_LENGTH} characters long."
            )
        # Require at least one uppercase, one lowercase, one digit, and one special char.
        if not re.search(r"[A-Z]", password):
            raise ValidationError("Password must contain at least one uppercase letter.")
        if not re.search(r"[a-z]", password):
            raise ValidationError("Password must contain at least one lowercase letter.")
        if not re.search(r"[0-9]", password):
            raise ValidationError("Password must contain at least one digit.")
        if not re.search(r"[!@#$%^&*()_+\-=[\]{};':\"\\|,.<>/?]", password):
            raise ValidationError("Password must contain at least one special character.")

    def _hash_password(self, password: str) -> str:
        """Hash a plain‑text password using bcrypt.

        Returns the hash as a UTF‑8 decoded string suitable for storage.
        """
        hashed = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
        return hashed.decode("utf-8")

    def _verify_password(self, password: str, stored_hash: str) -> bool:
        """Verify a password against the stored bcrypt hash.
        """
        try:
            return bcrypt.checkpw(password.encode("utf-8"), stored_hash.encode("utf-8"))
        except ValueError:
            # If the stored hash is malformed, treat as verification failure.
            return False

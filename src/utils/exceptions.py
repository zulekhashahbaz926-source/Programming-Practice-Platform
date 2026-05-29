class AppError(Exception):
    """Base class for application-specific errors."""

class ValidationError(AppError):
    """Raised when input validation fails."""

class AuthenticationError(AppError):
    """Raised for authentication failures (invalid credentials, duplicate user, etc.)."""

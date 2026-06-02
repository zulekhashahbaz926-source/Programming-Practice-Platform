class ZyntrivaError(Exception):
    """Base exception for Zyntriva error handling."""


class ValidationError(ZyntrivaError):
    """Raised when user input validation fails."""


class AuthenticationError(ZyntrivaError):
    """Raised when authentication or login fails."""


class DatabaseError(ZyntrivaError):
    """Raised when database operations fail."""

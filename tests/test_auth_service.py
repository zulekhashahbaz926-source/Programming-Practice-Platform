import pytest
from src.auth.auth_service import AuthService
from src.utils.exceptions import ValidationError, AuthenticationError

def test_register_and_login_success(db):
    service = AuthService()
    # Register a new user
    user = service.register(username="testuser", password="Password1!", email="test@example.com")
    assert user.id is not None
    assert user.username == "testuser"
    # Login with correct credentials
    logged_in = service.login(username="testuser", password="Password1!")
    assert logged_in.id == user.id

def test_register_duplicate_username(db):
    service = AuthService()
    service.register(username="dupuser", password="Password1!", email="a@b.com")
    with pytest.raises(AuthenticationError):
        service.register(username="dupuser", password="Password2@", email="c@d.com")

def test_register_invalid_username(db):
    service = AuthService()
    with pytest.raises(ValidationError):
        service.register(username="ab", password="Password1!", email="test@example.com")

def test_login_invalid_credentials(db):
    service = AuthService()
    service.register(username="user1", password="Password1!", email="test@example.com")
    with pytest.raises(AuthenticationError):
        service.login(username="user1", password="WrongPass1!")
    with pytest.raises(AuthenticationError):
        service.login(username="nonexistent", password="Password1!")

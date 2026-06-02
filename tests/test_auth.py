import unittest
from auth.auth_controller import AuthController
from utils.exceptions import AuthenticationError, ValidationError
from database.db_manager import DatabaseManager

class TestAuthController(unittest.TestCase):
    def setUp(self):
        self.db = DatabaseManager(":memory:")
        self.db.initialize_schema()
        self.controller = AuthController(self.db)

    def test_register_and_authenticate_success(self):
        self.controller.register_user(
            full_name="Test User",
            username="tester",
            email="tester@zyntriva.com",
            password="SecurePass123",
            confirm_password="SecurePass123",
        )
        user = self.controller.authenticate_user("tester", "SecurePass123")
        self.assertEqual(user["username"], "tester")
        self.assertEqual(user["email"], "tester@zyntriva.com")

    def test_duplicate_user_rejected(self):
        self.controller.register_user(
            full_name="Test User",
            username="tester",
            email="tester@zyntriva.com",
            password="SecurePass123",
            confirm_password="SecurePass123",
        )
        with self.assertRaises(ValidationError):
            self.controller.register_user(
                full_name="Test User Two",
                username="tester",
                email="tester2@zyntriva.com",
                password="SecurePass123",
                confirm_password="SecurePass123",
            )

    def test_invalid_password_raises_error(self):
        with self.assertRaises(ValidationError):
            self.controller.register_user(
                full_name="Invalid User",
                username="invalid",
                email="invalid@zyntriva.com",
                password="short",
                confirm_password="short",
            )

    def test_wrong_password_fails_authentication(self):
        self.controller.register_user(
            full_name="Test User",
            username="tester",
            email="tester@zyntriva.com",
            password="SecurePass123",
            confirm_password="SecurePass123",
        )
        with self.assertRaises(AuthenticationError):
            self.controller.authenticate_user("tester", "WrongPassword")

    def test_missing_credentials_raises_authentication_error(self):
        with self.assertRaises(AuthenticationError):
            self.controller.authenticate_user("", "")

if __name__ == "__main__":
    unittest.main()

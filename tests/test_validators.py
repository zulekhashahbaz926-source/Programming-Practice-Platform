import unittest
from utils.validators import validate_email, validate_password, validate_username

class TestValidators(unittest.TestCase):
    def test_email_validation(self):
        self.assertTrue(validate_email("student@zyntriva.com"))
        self.assertFalse(validate_email("invalid-email"))

    def test_password_validation(self):
        self.assertTrue(validate_password("StrongPass1"))
        self.assertFalse(validate_password("short"))

    def test_username_validation(self):
        self.assertTrue(validate_username("user123"))
        self.assertFalse(validate_username("us"))
        self.assertFalse(validate_username("user space"))

if __name__ == "__main__":
    unittest.main()

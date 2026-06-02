import unittest
from database.db_manager import DatabaseManager

class TestDatabaseManager(unittest.TestCase):
    def setUp(self):
        self.db = DatabaseManager(":memory:")
        self.db.initialize_schema()

    def test_create_user_and_retrieve(self):
        user_id = self.db.create_user(
            full_name="Database Tester",
            username="dbtester",
            email="dbtester@zyntriva.com",
            password="hashed-password",
        )
        self.assertGreater(user_id, 0)
        row = self.db.find_user_by_username("dbtester")
        self.assertIsNotNone(row)
        self.assertEqual(row["email"], "dbtester@zyntriva.com")

    def test_notification_inserts_and_fetches(self):
        user_id = self.db.create_user(
            full_name="Notify User",
            username="notify",
            email="notify@zyntriva.com",
            password="hashed-password",
        )
        self.db.create_notification("Update Ready", "A new module has been released.", user_id)
        notifications = self.db.get_notifications(user_id)
        self.assertTrue(len(notifications) >= 1)
        self.assertEqual(notifications[0]["title"], "Update Ready")

if __name__ == "__main__":
    unittest.main()

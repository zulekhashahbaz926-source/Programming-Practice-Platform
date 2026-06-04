class TestingModule:
    def __init__(self, db):
        self.db = db

    def get_overview(self):
        tests = self.db.fetchall("SELECT * FROM tests ORDER BY id DESC LIMIT 5") if self.db else []
        test_list = [f"{row['name']}: {row['status']}" for row in tests]
        return {
            "title": "Testing and Automation",
            "overview": "Explore unit testing and automated testing concepts with example test cases and validation workflows.",
            "sections": [
                {
                    "title": "Unit Testing Concepts",
                    "text": "Unit testing ensures individual functions and classes behave as expected.",
                },
                {
                    "title": "Automated Testing Lab",
                    "text": "Automated tests catch regressions early and support continuous integration.",
                    "list": test_list,
                },
                {
                    "title": "Example Test Scripts",
                    "text": "The application includes unittest examples for authentication, database operations, and validation logic.",
                },
            ],
        }

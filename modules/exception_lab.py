class ExceptionLabModule:
    def __init__(self, db=None):
        self.db = db

    def get_overview(self):
        return {
            "title": "Exception Handling Lab",
            "overview": "Practice robust exception handling using try/except patterns, custom exceptions, file operations, and database safeguards.",
            "sections": [
                {
                    "title": "Try/Except in Practice",
                    "text": "Use structured exception handling to protect execution flows and provide meaningful feedback when errors occur.",
                    "list": [
                        "Catch specific exceptions instead of generic errors.",
                        "Log exceptions to create a traceable audit history.",
                        "Handle database errors gracefully and recover when possible.",
                    ],
                },
                {
                    "title": "Custom Exception Patterns",
                    "text": "Custom exceptions make error handling explicit and improve team communication about failure modes.",
                },
                {
                    "title": "File and Database Errors",
                    "text": "Demonstrating file-not-found and database connection exceptions helps students build resilient applications.",
                },
            ],
        }

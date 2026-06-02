class RefactoringModule:
    def __init__(self, db=None):
        self.db = db

    def get_overview(self):
        return {
            "title": "Refactoring & Code Quality",
            "overview": "Learn clean code principles, eliminate code smells, and improve legacy code with professional refactoring techniques.",
            "sections": [
                {
                    "title": "Bad Code vs Refactored Code",
                    "text": "Refactoring improves maintainability, readability, and extensibility without changing behavior.",
                    "list": [
                        "Extract methods to reduce duplication.",
                        "Use meaningful naming for classes and variables.",
                        "Simplify conditional expressions and remove dead code.",
                    ],
                },
                {
                    "title": "Code Smell Guide",
                    "text": "Recognize common smells such as long methods, duplicated logic, and inconsistent naming.",
                },
                {
                    "title": "Refactoring Tips",
                    "text": "Refactor incrementally, preserve tests, and maintain a clean architecture as features evolve.",
                },
            ],
        }

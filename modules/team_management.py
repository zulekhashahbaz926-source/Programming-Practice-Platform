class TeamManagementModule:
    def __init__(self, db=None):
        self.db = db

    def get_overview(self):
        return {
            "title": "Team Management",
            "overview": "Track team roles, contributions, and learning outcomes to support collaborative software engineering projects.",
            "sections": [
                {
                    "title": "Team Member Profiles",
                    "text": "Each team member contributes a role, expertise, and responsibilities for successful delivery.",
                    "list": [
                        "Project lead: coordinates requirements and releases.",
                        "Developer: implements features and refactors code.",
                        "Tester: validates test cases and ensures quality.",
                        "Reviewer: performs peer review and feedback analysis.",
                    ],
                },
                {
                    "title": "Contribution Tracker",
                    "text": "Capture contributions and learning outcomes to make team progress visible during each iteration.",
                },
                {
                    "title": "Learning Outcomes",
                    "text": "Reflect on software engineering practices, process improvement, refactoring, and deployment readiness.",
                },
            ],
        }

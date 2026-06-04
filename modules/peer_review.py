class PeerReviewModule:
    def __init__(self, db=None):
        self.db = db

    def get_overview(self):
        return {
            "title": "Peer Review Module",
            "overview": "Manage walkthroughs, inspection forms, team feedback, and review status tracking for collaborative quality assurance.",
            "sections": [
                {
                    "title": "Review Checklist",
                    "text": "A structured checklist improves code review efficiency and ensures style, design, and logic are validated.",
                    "list": [
                        "Clarity of variable and function names.",
                        "Correctness of algorithm logic.",
                        "Consistency with coding standards.",
                        "Completeness of documentation and comments.",
                    ],
                },
                {
                    "title": "Inspection Forms",
                    "text": "Inspection forms help capture findings, prioritize bugs, and assign follow-up actions.",
                },
                {
                    "title": "Review Status Tracking",
                    "text": "Keep team feedback visible and maintain a history of walkthrough decisions and improvement outcomes.",
                },
            ],
        }

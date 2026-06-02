from database.db_manager import DatabaseManager
from modules.process_model import ProcessModelModule
from modules.version_control import VersionControlModule
from modules.refactoring import RefactoringModule
from modules.testing_module import TestingModule
from modules.exception_lab import ExceptionLabModule
from modules.peer_review import PeerReviewModule
from modules.deployment import DeploymentModule
from modules.team_management import TeamManagementModule

class DashboardController:
    def __init__(self, db: DatabaseManager):
        self.db = db
        self.module_classes = {
            "Dashboard": None,
            "Process Models": ProcessModelModule,
            "Version Control": VersionControlModule,
            "Refactoring": RefactoringModule,
            "Testing": TestingModule,
            "Exception Lab": ExceptionLabModule,
            "Peer Review": PeerReviewModule,
            "Deployment": DeploymentModule,
            "Team Management": TeamManagementModule,
            "User & SPI Settings": None,
        }

    def get_dashboard_stats(self) -> dict:
        return self.db.get_stat_counts()

    def get_notifications(self, user_id: int):
        return self.db.get_notifications(user_id)

    def get_recent_activity(self):
        return self.db.get_recent_activity()

    def get_commits(self):
        return self.db.get_commits()

    def load_module_data(self, module_name: str):
        module_class = self.module_classes.get(module_name)
        if module_class is None:
            if module_name == "User & SPI Settings":
                return {
                    "title": "User & SPI Settings",
                    "overview": "Manage your profile, team process improvement settings, and learning progress from one unified pane.",
                    "sections": [
                        {
                            "title": "Profile Management",
                            "text": "Update your display name, username, and notification preferences. Keep your software engineering profile current for better practice tracking.",
                        },
                        {
                            "title": "SPI Configuration",
                            "text": "Configure your process improvement goals, set quality metrics, and review team performance indicators as part of your professional learning workflow.",
                        },
                    ],
                }
            return {
                "title": "Welcome to Zyntriva CodeForge",
                "overview": "Use the sidebar to explore process models, version control, refactoring, testing, peer review, deployment, and team management modules.",
                "sections": [],
            }
        module = module_class(self.db)
        return module.get_overview()

    def search_content(self, query: str) -> list:
        return [
            x for x in self.db.get_quizzes()
            if query.lower() in x["title"].lower() or query.lower() in x["description"].lower()
        ]

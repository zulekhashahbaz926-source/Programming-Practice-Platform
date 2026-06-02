class VersionControlModule:
    def __init__(self, db):
        self.db = db

    def get_overview(self):
        commits = self.db.get_commits() if self.db else []
        commit_list = [f"{commit['timestamp'].split('T')[0]}: {commit['message']}" for commit in commits]
        return {
            "title": "Version Control Simulator",
            "overview": "Simulate Git-style workflows and understand commit history, branches, push/pull concepts, and version tracking.",
            "sections": [
                {
                    "title": "Git Concepts Explained",
                    "text": "Branching allows parallel development, while commits capture meaningful change sets along the lifecycle of the repository.",
                },
                {
                    "title": "Commit History Viewer",
                    "text": "The platform stores version history logs and explains how each commit contributes to software maintenance.",
                    "list": commit_list,
                },
                {
                    "title": "Push and Pull Workflow",
                    "text": "Push sends changes to the remote repository and pull integrates upstream updates into the local branch.",
                },
            ],
        }

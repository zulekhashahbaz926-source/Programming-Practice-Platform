class ProcessModelModule:
    def __init__(self, db=None):
        self.db = db

    def get_overview(self):
        return {
            "title": "Process Model Learning",
            "overview": "Explore software process models and learn how Agile, Waterfall, Spiral, Incremental, and RAD approaches shape engineering practice.",
            "sections": [
                {
                    "title": "Theory of Modern Process Models",
                    "text": "Understanding different process models helps teams choose the right lifecycle for planning, implementation, testing, and maintenance.",
                },
                {
                    "title": "Comparing Process Models",
                    "text": "Each model enforces discipline in different ways. The table below describes core strengths and when to use each.",
                    "list": [
                        "Waterfall: Predictable and phase-based for stable requirements.",
                        "Agile: Iterative, customer-focused, and adaptive for evolving requirements.",
                        "Spiral: Risk-driven with continuous evaluation and prototyping.",
                        "Incremental: Delivers value gradually through repeated builds.",
                        "RAD: Rapid application development for time-sensitive projects.",
                    ],
                },
                {
                    "title": "Quiz and Reflection",
                    "text": "Use the quiz questions to validate understanding of process model selection and software process improvement.",
                },
            ],
        }

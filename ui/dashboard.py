import customtkinter as ctk


class DashboardScreen(ctk.CTkFrame):
    """Main dashboard after login.

    Shows basic user info and navigation buttons to other screens.
    """

    def __init__(self, master, user, on_lessons, on_practice, on_quiz, on_progress, on_leaderboard, **kwargs):
        super().__init__(master, **kwargs)
        self.master = master
        self.user = user
        self.on_lessons = on_lessons
        self.on_practice = on_practice
        self.on_quiz = on_quiz
        self.on_progress = on_progress
        self.on_leaderboard = on_leaderboard
        self.configure(fg_color="#2B2B2B")
        self._build_ui()

    def _build_ui(self):
        # Welcome label
        welcome = ctk.CTkLabel(self, text=f"Welcome, {self.user[1]}!", font=("Helvetica", 20, "bold"), text_color="#FFFFFF")
        welcome.pack(pady=20)
        # Navigation buttons
        btn_cfg = {"width": 200, "fg_color": "#374151", "hover_color": "#4B5563"}
        ctk.CTkButton(self, text="Lessons", command=self.on_lessons, **btn_cfg).pack(pady=8)
        ctk.CTkButton(self, text="Practice", command=self.on_practice, **btn_cfg).pack(pady=8)
        ctk.CTkButton(self, text="Quizzes", command=self.on_quiz, **btn_cfg).pack(pady=8)
        # New buttons for progress and leaderboard
        ctk.CTkButton(self, text="Progress", command=self.on_progress, **btn_cfg).pack(pady=8)
        ctk.CTkButton(self, text="Leaderboard", command=self.on_leaderboard, **btn_cfg).pack(pady=8)
        # Placeholder for future features
        extra = ["Notes"]
        for name in extra:
            ctk.CTkButton(self, text=name, width=200).pack(pady=8)

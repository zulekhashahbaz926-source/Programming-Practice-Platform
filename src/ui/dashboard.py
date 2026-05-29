import customtkinter as ctk
from typing import Callable

class Dashboard(ctk.CTkFrame):
    """Main dashboard view.

    Parameters
    ----------
    master: ctk.CTk
        Parent window.
    navigate: Callable[[str], None]
        Function to change view, expects view name.
    """
    def __init__(self, master, navigate: Callable[[str], None]):
        super().__init__(master)
        self.navigate = navigate
        self.configure(fg_color="transparent")
        self._build_sidebar()
        self._build_overview()

    def _build_sidebar(self):
        sidebar = ctk.CTkFrame(self, width=200, corner_radius=0)
        sidebar.pack(side="left", fill="y")
        btn_ex = ctk.CTkButton(sidebar, text="Exercises", command=lambda: self.navigate('exercise'))
        btn_ch = ctk.CTkButton(sidebar, text="Challenges", command=lambda: self.navigate('challenge'))
        btn_set = ctk.CTkButton(sidebar, text="Settings", command=lambda: self.navigate('settings'))
        for btn in (btn_ex, btn_ch, btn_set):
            btn.pack(pady=10, padx=20, fill="x")

    def _build_overview(self):
        # Placeholder cards – UI only, data will be filled by a controller later
        content = ctk.CTkFrame(self)
        content.pack(side="right", expand=True, fill="both", padx=20, pady=20)
        # Card 1: Completed exercises
        card1 = ctk.CTkFrame(content, corner_radius=10, height=100)
        card1.pack(fill="x", pady=10)
        ctk.CTkLabel(card1, text="Completed Exercises", font=("Arial", 14)).pack(pady=5)
        self.completed_label = ctk.CTkLabel(card1, text="0", font=("Arial", 24))
        self.completed_label.pack()
        # Card 2: Total Score
        card2 = ctk.CTkFrame(content, corner_radius=10, height=100)
        card2.pack(fill="x", pady=10)
        ctk.CTkLabel(card2, text="Total Score", font=("Arial", 14)).pack(pady=5)
        self.score_label = ctk.CTkLabel(card2, text="0", font=("Arial", 24))
        self.score_label.pack()
        # Card 3: Accuracy
        card3 = ctk.CTkFrame(content, corner_radius=10, height=100)
        card3.pack(fill="x", pady=10)
        ctk.CTkLabel(card3, text="Accuracy", font=("Arial", 14)).pack(pady=5)
        self.accuracy_label = ctk.CTkLabel(card3, text="0%", font=("Arial", 24))
        self.accuracy_label.pack()

    # Public methods for UI controller to update stats
    def update_stats(self, completed: int, score: float, accuracy: float):
        self.completed_label.configure(text=str(completed))
        self.score_label.configure(text=f"{score:.1f}")
        self.accuracy_label.configure(text=f"{accuracy:.1%}")

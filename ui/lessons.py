import customtkinter as ctk

class LessonsScreen(ctk.CTkFrame):
    """Screen showing a list of lessons. Currently placeholder content.

    Parameters
    ----------
    master: ctk.CTk
        The root window.
    on_back: callable
        Callback to return to the dashboard.
    """

    def __init__(self, master, on_back, **kwargs):
        super().__init__(master, **kwargs)
        self.master = master
        self.on_back = on_back
        self.configure(fg_color="#2B2B2B")
        self._build_ui()

    def _build_ui(self):
        # Header with back button
        header = ctk.CTkFrame(self, fg_color="transparent")
        header.pack(fill="x", pady=(10, 0))
        back_btn = ctk.CTkButton(header, text="← Back", width=80, command=self.on_back)
        back_btn.pack(side="left", padx=10)
        title = ctk.CTkLabel(header, text="Lessons", font=("Helvetica", 20, "bold"), text_color="white")
        title.pack(side="left", padx=20)

        # Scrollable list of lessons (placeholder)
        lessons_frame = ctk.CTkScrollableFrame(self)
        lessons_frame.pack(fill="both", expand=True, pady=20, padx=20)
        lesson_names = [
            "Python Basics",
            "C++ Fundamentals",
            "Java Intro",
            "Data Structures",
            "Algorithms",
        ]
        for name in lesson_names:
            btn = ctk.CTkButton(lessons_frame, text=name, width=300, anchor="w")
            btn.pack(pady=5, fill="x")

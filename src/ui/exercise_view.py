import customtkinter as ctk
from typing import Callable

from src.core.exercise_manager import ExerciseManager
from src.utils.exceptions import ValidationError

class ExerciseViewPage(ctk.CTkFrame):
    """Exercise view allowing code entry and submission.

    UI only – delegates all logic to :class:`ExerciseManager`.
    """

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.manager = ExerciseManager()
        self.current_exercise_id = None
        self._build_ui()
        self.load_random_exercise()

    def _build_ui(self):
        # Title
        self.title_label = ctk.CTkLabel(self, text="Exercise", font=("Helvetica", 20, "bold"))
        self.title_label.pack(pady=10)

        # Description area
        self.desc = ctk.CTkLabel(self, text="", wraplength=800, justify="left")
        self.desc.pack(pady=5)

        # Code editor – using CTkTextbox (multiline)
        self.editor = ctk.CTkTextbox(self, width=800, height=300)
        self.editor.pack(pady=10)

        # Buttons
        btn_frame = ctk.CTkFrame(self)
        btn_frame.pack(pady=5)
        self.run_btn = ctk.CTkButton(btn_frame, text="Run", command=self.run_code)
        self.submit_btn = ctk.CTkButton(btn_frame, text="Submit", command=self.submit_code)
        self.run_btn.grid(row=0, column=0, padx=5)
        self.submit_btn.grid(row=0, column=1, padx=5)

        # Feedback label
        self.feedback = ctk.CTkLabel(self, text="", wraplength=800)
        self.feedback.pack(pady=10)

        # Navigation back button
        self.back_btn = ctk.CTkButton(self, text="Back to Dashboard", command=lambda: self.controller.show_frame("Dashboard"))
        self.back_btn.pack(pady=5)

    def load_random_exercise(self):
        """Pick a random exercise from the manager and populate UI.
        """
        exercises = self.manager.list_exercises()
        if not exercises:
            self.title_label.configure(text="No exercises available")
            return
        import random
        ex = random.choice(exercises)
        self.current_exercise_id = ex.id
        self.title_label.configure(text=ex.title)
        self.desc.configure(text=ex.description or "")
        self.editor.delete("1.0", ctk.END)
        self.feedback.configure(text="")

    def run_code(self):
        """Placeholder for running code – simply echoes the editor content.
        """
        code = self.editor.get("1.0", ctk.END).strip()
        if not code:
            self.feedback.configure(text="Please enter code before running.", text_color="red")
            return
        # In a real app, sandboxed execution would occur here.
        self.feedback.configure(text="[Run] Code received (execution sandbox not implemented).", text_color="orange")

    def submit_code(self):
        """Submit the user code to the ExerciseManager for evaluation.
        """
        if self.current_exercise_id is None:
            self.feedback.configure(text="No exercise loaded.", text_color="red")
            return
        code = self.editor.get("1.0", ctk.END).strip()
        try:
            correct, msg = self.manager.evaluate_submission(self.current_exercise_id, code)
            color = "green" if correct else "red"
            self.feedback.configure(text=msg, text_color=color)
        except ValidationError as e:
            self.feedback.configure(text=str(e), text_color="red")
        except Exception as e:
            self.feedback.configure(text=f"Unexpected error: {e}", text_color="red")

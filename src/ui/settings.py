import customtkinter as ctk
from typing import Callable

class SettingsPage(ctk.CTkFrame):
    """Simple settings page.

    Provides a theme toggle (light/dark) and a placeholder for future preferences.
    """
    def __init__(self, parent, controller: Callable[[str], None]):
        super().__init__(parent)
        self.controller = controller
        self._build_ui()

    def _build_ui(self):
        # Title
        title = ctk.CTkLabel(self, text="Settings", font=("Helvetica", 20, "bold"))
        title.pack(pady=20)

        # Theme toggle button – switches between Light and Dark
        def toggle_theme():
            current = ctk.get_appearance_mode()
            new_mode = "Dark" if current == "Light" else "Light"
            ctk.set_appearance_mode(new_mode)
            self.theme_label.configure(text=f"Current theme: {new_mode}")

        self.theme_label = ctk.CTkLabel(self, text=f"Current theme: {ctk.get_appearance_mode()}")
        self.theme_label.pack(pady=10)

        toggle_btn = ctk.CTkButton(self, text="Toggle Theme", command=toggle_theme)
        toggle_btn.pack(pady=10)

        # Back button to return to dashboard
        back_btn = ctk.CTkButton(self, text="Back to Dashboard", command=lambda: self.controller.show_frame("Dashboard"))
        back_btn.pack(pady=20)

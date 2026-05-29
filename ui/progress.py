import customtkinter as ctk

class ProgressScreen(ctk.CTkFrame):
    """Display user's progress stats. Placeholder for future charts.

    Parameters
    ----------
    master: ctk.CTk
        Root window.
    on_back: callable
        Callback to return to dashboard.
    """

    def __init__(self, master, on_back, **kwargs):
        super().__init__(master, **kwargs)
        self.on_back = on_back
        self.configure(fg_color="#2B2B2B")
        self._build_ui()

    def _build_ui(self):
        # Header with back button
        header = ctk.CTkFrame(self, fg_color="transparent")
        header.pack(fill="x", pady=5)
        ctk.CTkButton(header, text="← Back", command=self.on_back, width=80).pack(side="left", padx=10)
        ctk.CTkLabel(header, text="Progress", font=("Helvetica", 20, "bold"), text_color="#FFFFFF").pack(side="left", padx=20)

        # Placeholder stats area
        body = ctk.CTkFrame(self, fg_color="transparent")
        body.pack(fill="both", expand=True, padx=20, pady=10)
        ctk.CTkLabel(body, text="Progress data will appear here.", font=("Helvetica", 16), text_color="#E5E7EB").pack(pady=40)

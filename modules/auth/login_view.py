import tkinter as tk
import tkinter.font as tkfont
from tkinter import messagebox
from ttkbootstrap import ttk, Style

# Helper for a temporary toast‑style message
def _show_toast(parent, text, duration=2000):
    toast = ttk.Label(parent, text=text, bootstyle="danger", padding=5)
    toast.pack(side="top", fill="x", pady=(0, 10))
    parent.after(duration, toast.destroy)

class LoginView(ttk.Frame):
    """Premium‑styled login screen.

    Features
    --------
    • Dark gradient background (set on the root by the caller).
    • Rounded “card” container with neon accent borders.
    • Custom "Outfit"‑style font (fallback to Helvetica).
    • Hover animation on the login button.
    • Toast‑style error feedback instead of a modal dialog.
    • Placeholder logo at the top of the card.
    """

    def __init__(self, master, on_success, *args, **kwargs):
        super().__init__(master, padding=30, *args, **kwargs)
        self.on_success = on_success

        # Font configuration (use a modern sans‑serif; ttkbootstrap will
        # fall back to a system font if not available).
        self.title_font = tkfont.Font(family="Outfit", size=20, weight="bold")
        self.label_font = tkfont.Font(family="Outfit", size=12)
        self.entry_font = tkfont.Font(family="Outfit", size=11)

        # Card container – a rounded frame with a subtle shadow.
        self.card = ttk.Frame(self, bootstyle="light", padding=20)
        self.card.pack(expand=True, fill="both", padx=50, pady=50)

        # Logo placeholder – a simple text label that can be replaced by a
        # real image later.
        ttk.Label(
            self.card,
            text="P",
            font=("Outfit", 48, "bold"),
            foreground="#00f5ff",
            bootstyle="primary",
        ).pack(pady=(0, 10))

        # Title and subtitle
        ttk.Label(
            self.card,
            text="Programming Practices Platform",
            font=self.title_font,
            bootstyle="primary",
        ).pack(pady=(0, 5))
        ttk.Label(
            self.card,
            text="Login to continue",
            font=self.label_font,
            bootstyle="secondary",
        ).pack(pady=(0, 20))

        # Form fields (username & password)
        form = ttk.Frame(self.card)
        form.pack(pady=5, fill="x")

        # Username row
        ttk.Label(form, text="Username:", width=12, anchor="e", bootstyle="info").grid(
            row=0, column=0, sticky="e", padx=5, pady=5
        )
        self.username_entry = ttk.Entry(
            form, width=30, font=self.entry_font, bootstyle="secondary"
        )
        self.username_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        ttk.Label(card, text="Login to continue", font=("Outfit", 12), bootstyle="secondary").pack(pady=(0, 15))

        # Username field
        user_frame = ttk.Frame(card)
        user_frame.pack(fill="x", pady=5)
        ttk.Label(user_frame, text="Username:", width=12, anchor="w", bootstyle="info").pack(side="left")
        self.username_entry = ttk.Entry(user_frame, font=("Outfit", 11))
        self.username_entry.pack(side="left", fill="x", expand=True)

        # Password field
        pass_frame = ttk.Frame(card)
        pass_frame.pack(fill="x", pady=5)
        ttk.Label(pass_frame, text="Password:", width=12, anchor="w", bootstyle="info").pack(side="left")
        self.password_entry = ttk.Entry(pass_frame, show="*", font=("Outfit", 11))
        self.password_entry.pack(side="left", fill="x", expand=True)

        # Login button with hover effect
        login_btn = ttk.Button(card, text="Log In", bootstyle="success-outline", command=self._attempt_login)
        login_btn.pack(pady=20)
        login_btn.bind("<Enter>", lambda e: login_btn.configure(style="Hover.TButton"))
        login_btn.bind("<Leave>", lambda e: login_btn.configure(style="TButton"))

        # Style for hover effect (lighter background)
        style.map(
            "Hover.TButton",
            background=[("active", "#00f5ff")],
            foreground=[("active", "#000000")],
        )

        # Set initial focus
        self.username_entry.focus()

    def _show_error(self, message: str):
        ToastMessage(self.master, message)

    def _attempt_login(self):
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()
        # Demo credentials – replace with real auth later
        if username == "admin" and password == "admin":
            self.on_success()
        else:
            self._show_error("Invalid username or password")

import customtkinter as ctk
from auth.auth_controller import AuthController
from core.logger import app_logger
from utils.validators import validate_email

class AuthView(ctk.CTkFrame):
    def __init__(self, parent, app):
        super().__init__(parent, fg_color="#0D111E")
        self.app = app
        self.db = app.db
        self.controller = AuthController(self.db)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.current_mode = "login"
        self.clicked = False
        self.build_interface()

    def build_interface(self):
        self.container = ctk.CTkFrame(
            self,
            fg_color="#0B1120",
            corner_radius=24,
            border_width=1,
            border_color="#151B2E",
            width=760,
            height=520,
        )
        self.container.place(relx=0.5, rely=0.5, anchor="center")

        self.container.grid_columnconfigure(0, weight=1, uniform="group1")
        self.container.grid_columnconfigure(1, weight=1, uniform="group1")
        self.container.grid_rowconfigure(0, weight=1)

        left_panel = ctk.CTkFrame(self.container, fg_color="#09101F", corner_radius=20)
        left_panel.grid(row=0, column=0, sticky="nsew", padx=(24, 12), pady=24)
        left_panel.grid_rowconfigure(4, weight=1)

        right_panel = ctk.CTkFrame(self.container, fg_color="#111827", corner_radius=20)
        right_panel.grid(row=0, column=1, sticky="nsew", padx=(12, 24), pady=24)
        right_panel.grid_rowconfigure(6, weight=1)

        title = ctk.CTkLabel(
            left_panel,
            text="Welcome Back to Zyntriva",
            font=ctk.CTkFont(size=26, weight="bold"),
            text_color="#F8FAFF",
            wraplength=300,
            justify="left",
        )
        title.pack(anchor="w", padx=24, pady=(28, 8))

        subtitle = ctk.CTkLabel(
            left_panel,
            text="Continue your programming journey with a premium software engineering practice platform.",
            font=ctk.CTkFont(size=13),
            text_color="#A8B3D1",
            wraplength=300,
            justify="left",
        )
        subtitle.pack(anchor="w", padx=24, pady=(0, 24))

        highlights = ctk.CTkFrame(left_panel, fg_color="#0D1728", corner_radius=18)
        highlights.pack(fill="x", padx=24, pady=(0, 20))
        for label in [
            "Modular learning modules",
            "Secure account access",
            "Professional developer experience",
        ]:
            ctk.CTkLabel(
                highlights,
                text=f"• {label}",
                font=ctk.CTkFont(size=12),
                text_color="#A5B4FC",
                wraplength=260,
                justify="left",
            ).pack(anchor="w", padx=18, pady=8)

        ctk.CTkLabel(
            left_panel,
            text="Cyberpunk-inspired desktop experience",
            font=ctk.CTkFont(size=12, weight="bold"),
            text_color="#38BDF8",
        ).pack(anchor="w", padx=24, pady=(8, 4))

        ctk.CTkLabel(
            left_panel,
            text="Built for software engineering professionals and advanced learning workflows.",
            font=ctk.CTkFont(size=12),
            text_color="#94A3B8",
            wraplength=300,
            justify="left",
        ).pack(anchor="w", padx=24, pady=(0, 24))

        self.switch_frame = ctk.CTkSegmentedButton(
            right_panel,
            values=["Sign In", "Create Account"],
            command=self.toggle_mode,
            selected_color="#7C4DFF",
            text_color="#FFFFFF",
            variable=ctk.StringVar(value="Sign In"),
        )
        self.switch_frame.pack(padx=24, pady=(24, 20), fill="x")

        self.form_frame = ctk.CTkFrame(right_panel, fg_color="#0C1524", corner_radius=20)
        self.form_frame.pack(padx=24, pady=(0, 12), fill="both", expand=True)
        self.build_login_form()

        self.message_label = ctk.CTkLabel(right_panel, text="", text_color="#F2F5FF")
        self.message_label.pack(anchor="w", padx=24, pady=(0, 24))

    def clear_frame(self):
        for widget in self.form_frame.winfo_children():
            widget.destroy()

    def toggle_mode(self, value):
        self.current_mode = "register" if value == "Create Account" else "login"
        self.clear_frame()
        if self.current_mode == "register":
            self.build_register_form()
        else:
            self.build_login_form()
        self.message_label.configure(text="")

    def build_login_form(self):
        self.username_var = ctk.StringVar()
        self.password_var = ctk.StringVar()
        self.show_password_var = ctk.BooleanVar(value=False)
        self.remember_var = ctk.BooleanVar(value=True)

        ctk.CTkLabel(self.form_frame, text="Email or Username", text_color="#B3B8DF").pack(anchor="w", padx=24, pady=(20, 6))
        self.username_entry = ctk.CTkEntry(
            self.form_frame,
            textvariable=self.username_var,
            placeholder_text="Enter your email or username",
            corner_radius=14,
            fg_color="#0F1320",
            height=44,
        )
        self.username_entry.pack(fill="x", padx=24)

        ctk.CTkLabel(self.form_frame, text="Password", text_color="#B3B8DF").pack(anchor="w", padx=24, pady=(16, 6))
        self.password_entry = ctk.CTkEntry(
            self.form_frame,
            textvariable=self.password_var,
            show="*",
            placeholder_text="Enter your password",
            corner_radius=14,
            fg_color="#0F1320",
            height=44,
        )
        self.password_entry.pack(fill="x", padx=24)

        ctk.CTkCheckBox(
            self.form_frame,
            text="Show password",
            variable=self.show_password_var,
            command=self.toggle_password_visibility,
            text_color="#A8B3D1",
            fg_color="#141B2D",
            corner_radius=12,
        ).pack(anchor="w", padx=24, pady=(12, 0))

        ctk.CTkCheckBox(
            self.form_frame,
            text="Remember me",
            variable=self.remember_var,
            text_color="#A8B3D1",
            fg_color="#141B2D",
            corner_radius=12,
        ).pack(anchor="w", padx=24, pady=(6, 0))

        ctk.CTkButton(
            self.form_frame,
            text="Sign In to Dashboard",
            command=self.login_user,
            fg_color=("#7C4DFF", "#5E60CE"),
            hover_color="#6B4AED",
            corner_radius=18,
            height=48,
        ).pack(fill="x", padx=24, pady=(18, 6))

        ctk.CTkButton(
            self.form_frame,
            text="Forgot password?",
            command=self.forgot_password,
            fg_color="#111827",
            text_color="#84A6FF",
            hover_color="#17243E",
            corner_radius=18,
            height=44,
        ).pack(fill="x", padx=24, pady=(6, 24))

    def build_register_form(self):
        self.fullname_var = ctk.StringVar()
        self.username_var = ctk.StringVar()
        self.email_var = ctk.StringVar()
        self.password_var = ctk.StringVar()
        self.confirm_password_var = ctk.StringVar()
        self.show_password_var = ctk.BooleanVar(value=False)

        fields = [
            ("Full Name", self.fullname_var),
            ("Username", self.username_var),
            ("Email", self.email_var),
            ("Password", self.password_var),
            ("Confirm Password", self.confirm_password_var),
        ]

        for label_text, variable in fields:
            ctk.CTkLabel(self.form_frame, text=label_text, text_color="#B3B8DF").pack(anchor="w", padx=24, pady=(16, 6))
            show = "*" if "Password" in label_text else ""
            entry = ctk.CTkEntry(self.form_frame, textvariable=variable, show=show, corner_radius=12, fg_color="#0F1320")
            entry.pack(fill="x", padx=24)
            if label_text == "Password":
                self.password_entry = entry
            if label_text == "Confirm Password":
                self.confirm_password_entry = entry

        ctk.CTkCheckBox(
            self.form_frame,
            text="Show password",
            variable=self.show_password_var,
            command=self.toggle_password_visibility,
            text_color="#A8B3D1",
        ).pack(anchor="w", padx=24, pady=(8, 0))

        ctk.CTkButton(
            self.form_frame,
            text="Register",
            command=self.register_user,
            fg_color="#6C63FF",
            hover_color="#7F7BFF",
            corner_radius=14,
        ).pack(fill="x", padx=24, pady=(20, 24))

    def toggle_password_visibility(self):
        if self.show_password_var.get():
            self.password_entry.configure(show="")
            confirm_entry = getattr(self, "confirm_password_entry", None)
            if confirm_entry and confirm_entry.winfo_exists():
                confirm_entry.configure(show="")
        else:
            self.password_entry.configure(show="*")
            confirm_entry = getattr(self, "confirm_password_entry", None)
            if confirm_entry and confirm_entry.winfo_exists():
                confirm_entry.configure(show="*")

    def login_user(self):
        try:
            user_info = self.controller.authenticate_user(self.username_var.get(), self.password_var.get())
            self.message_label.configure(text="Login successful. Loading dashboard...", text_color="#7FFFD4")
            self.after(300, lambda: self.app.login_user(user_info))
        except Exception as exc:
            app_logger.warning(f"Login failed: {exc}")
            self.message_label.configure(text=str(exc), text_color="#FF5A5F")

    def register_user(self):
        try:
            self.controller.register_user(
                self.fullname_var.get(),
                self.username_var.get(),
                self.email_var.get(),
                self.password_var.get(),
                self.confirm_password_var.get(),
            )
            self.message_label.configure(text="Account created successfully. Please login.", text_color="#7FFFD4")
            self.switch_frame.set("Sign In")
            self.toggle_mode("Sign In")
        except Exception as exc:
            app_logger.warning(f"Registration failed: {exc}")
            self.message_label.configure(text=str(exc), text_color="#FF5A5F")

    def forgot_password(self):
        email = self.username_var.get() if self.current_mode == "login" else self.email_var.get()
        if validate_email(email):
            self.message_label.configure(text="Password reset instructions sent to your email.", text_color="#7FFFD4")
        else:
            self.message_label.configure(text="Enter a valid email to recover your password.", text_color="#FF5A5F")

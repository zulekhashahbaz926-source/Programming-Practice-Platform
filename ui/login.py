import customtkinter as ctk

class LoginScreen(ctk.CTkFrame):
    """Login and signup UI.

    Parameters
    ----------
    master: ctk.CTk
        The root window.
    on_login: callable(email: str, password: str)
        Callback when the user clicks the Login button.
    on_signup: callable(name: str, email: str, password: str)
        Callback when the user clicks the Sign Up button.
    """

    def __init__(self, master, on_login, on_signup, **kwargs):
        super().__init__(master, **kwargs)
        self.on_login = on_login
        self.on_signup = on_signup
        self._build_ui()

    def _build_ui(self):
        ctk.set_appearance_mode("dark")
        self.configure(fg_color="#2b2b2b")

        # Title
        self.title_label = ctk.CTkLabel(self, text="Programming Practices Platform", font=("Helvetica", 24, "bold"), text_color="white")
        self.title_label.pack(pady=20)

        # Name (only needed for signup)
        self.name_entry = ctk.CTkEntry(self, placeholder_text="Name (for Sign Up)")
        self.name_entry.pack(pady=10, fill="x", padx=50)

        # Email
        self.email_entry = ctk.CTkEntry(self, placeholder_text="Email")
        self.email_entry.pack(pady=10, fill="x", padx=50)

        # Password
        self.password_entry = ctk.CTkEntry(self, placeholder_text="Password", show="*")
        self.password_entry.pack(pady=10, fill="x", padx=50)

        # Info / error label
        self.message_label = ctk.CTkLabel(self, text="", text_color="#ff6b6b")
        self.message_label.pack(pady=5)

        # Buttons container
        btn_frame = ctk.CTkFrame(self, fg_color="transparent")
        btn_frame.pack(pady=15)

        self.login_btn = ctk.CTkButton(btn_frame, text="Login", command=self._login)
        self.login_btn.grid(row=0, column=0, padx=10)

        self.signup_btn = ctk.CTkButton(btn_frame, text="Sign Up", command=self._signup)
        self.signup_btn.grid(row=0, column=1, padx=10)

    def _login(self):
        email = self.email_entry.get().strip()
        password = self.password_entry.get().strip()
        if not email or not password:
            self.show_error("Please provide email and password")
            return
        self.on_login(email, password)

    def _signup(self):
        name = self.name_entry.get().strip()
        email = self.email_entry.get().strip()
        password = self.password_entry.get().strip()
        if not name or not email or not password:
            self.show_error("All fields are required for Sign Up")
            return
        self.on_signup(name, email, password)

    # Helper methods for messages
    def show_error(self, message: str):
        self.message_label.configure(text=message, text_color="#ff6b6b")

    def show_info(self, message: str):
        self.message_label.configure(text=message, text_color="#6bffb8")

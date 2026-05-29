import customtkinter as ctk
import tkinter as tk
# Import authentication helpers from backend
from backend.db import init_db, get_user_by_email, create_user, verify_password
from ui.login import LoginScreen
from ui.dashboard import DashboardScreen
from ui.lessons import LessonsScreen
from ui.practice import PracticeScreen
from ui.quiz import QuizScreen

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Programming Practices Platform")
        self.geometry("900x600")
        self.resizable(False, False)
        self.current_user = None
        # Initialize DB
        init_db()
        # Start with login screen
        self.show_login()

    def show_login(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.login_screen = LoginScreen(self, on_login=self.handle_login, on_signup=self.handle_signup)
        self.login_screen.pack(fill="both", expand=True)

    def handle_login(self, email, password):
        user = get_user_by_email(email)
        if user and verify_password(password, user[4]):  # password hash at index 4
            self.current_user = user
            self.show_dashboard()
        else:
            self.login_screen.show_error("Invalid credentials")

    def handle_signup(self, name, email, password):
        if get_user_by_email(email):
            self.login_screen.show_error("Email already registered")
            return
        create_user(name, email, password)
        self.login_screen.show_info("Account created. Please login.")

    def show_dashboard(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.dashboard = DashboardScreen(
            self,
            user=self.current_user,
            on_lessons=self.show_lessons,
            on_practice=self.show_practice,
            on_quiz=self.show_quiz,
            on_progress=self.show_progress,
            on_leaderboard=self.show_leaderboard
        )
        self.dashboard.pack(fill="both", expand=True)

    def show_lessons(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.lessons_screen = LessonsScreen(self, on_back=self.show_dashboard)
        self.lessons_screen.pack(fill="both", expand=True)

    def show_practice(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.practice_screen = PracticeScreen(self, on_back=self.show_dashboard)
        self.practice_screen.pack(fill="both", expand=True)

    def show_quiz(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.quiz_screen = QuizScreen(self, on_back=self.show_dashboard)
        self.quiz_screen.pack(fill="both", expand=True)

if __name__ == "__main__":
    app = App()
    app.mainloop()



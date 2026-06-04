import customtkinter as ctk
from config.settings import APP_NAME, DEFAULT_THEME
from database.db_manager import DatabaseManager
from database.seed_data import seed_sample_data
from core.theme_manager import ThemeManager
from core.logger import app_logger
from auth.auth_views import AuthView
from dashboard.dashboard_views import DashboardView

class ZyntrivaApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title(f"{APP_NAME} – Programming Practices Platform")
        self.geometry("1280x760")
        self.minsize(1150, 720)
        ThemeManager.apply_theme(DEFAULT_THEME)

        self.db = DatabaseManager()
        self.db.initialize_schema()
        seed_sample_data(self.db)

        self.current_user = None
        self.frames = {}

        container = ctk.CTkFrame(self, fg_color="#0F1320")
        container.pack(fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        for FrameClass in (AuthView, DashboardView):
            frame = FrameClass(parent=container, app=self)
            self.frames[FrameClass.__name__] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("AuthView")

    def show_frame(self, name: str):
        frame = self.frames.get(name)
        if frame:
            frame.tkraise()
            if hasattr(frame, "refresh"):
                frame.refresh()

    def login_user(self, user: dict):
        self.current_user = user
        app_logger.info(f"User logged in: {user.get('username')}")
        self.show_frame("DashboardView")

    def logout_user(self):
        app_logger.info("User logged out.")
        self.current_user = None
        self.show_frame("AuthView")

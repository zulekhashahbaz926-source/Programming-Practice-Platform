import tkinter as tk
from customtkinter import CTk

from src.ui.main_window import MainWindow
from src.core.app_state import AppState
from src.utils.logger import get_logger

class App(CTk):
    """Main application class inheriting from CustomTkinter's CTk.

    It sets up the logger, application state, and the main UI window.
    """

    def __init__(self):
        super().__init__()
        self.title("Programming Practices Platform")
        self.geometry("1024x768")
        self.resizable(True, True)
        # Initialize logger
        self.logger = get_logger(__name__)
        self.logger.info("Application started")
        # Initialize shared application state
        self.state = AppState()
        # Initialize UI
        self.main_window = MainWindow(self, self.state)
        self.main_window.pack(fill="both", expand=True)

    def run(self):
        self.logger.info("Entering main loop")
        self.mainloop()

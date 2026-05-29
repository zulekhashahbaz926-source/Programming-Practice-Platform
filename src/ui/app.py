"""UI router and main application for the Programming Practices Platform.

This module creates a CustomTkinter based window with a persistent sidebar for
navigation and a frame container that swaps between the concrete UI pages:
Dashboard, ExerciseView, and Settings.

The UI layer imports **service** classes from ``src.core`` but does not contain
any business logic – all operations are delegated to those services.
"""

import customtkinter as ctk
from typing import Dict

# Import UI pages – they are defined in sibling modules.
from .dashboard import DashboardPage
from .exercise_view import ExerciseViewPage
from .settings import SettingsPage


class App(ctk.CTk):
    """Root application window with a sidebar navigator.

    The router holds a mapping ``self.frames`` of page name -> frame instance.
    ``show_frame`` raises the selected frame to the top of the stacking order.
    """

    def __init__(self):
        super().__init__()
        self.title("Programming Practices Platform")
        self.geometry("1200x800")
        self.resizable(True, True)

        # Theme management – default to system mode; can be overridden via Settings.
        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("blue")

        # -----------------------------------------------------------------
        # Layout: a persistent sidebar on the left and a content area.
        # -----------------------------------------------------------------
        self.sidebar = ctk.CTkFrame(self, width=200, corner_radius=0)
        self.sidebar.pack(side="left", fill="y")

        self.container = ctk.CTkFrame(self, corner_radius=0)
        self.container.pack(side="right", fill="both", expand=True)

        # Initialise frames dictionary.
        self.frames: Dict[str, ctk.CTkFrame] = {}
        self._create_frames()
        self._populate_sidebar()

        # Show default page.
        self.show_frame("Dashboard")

    # ---------------------------------------------------------------------
    # Frame handling
    # ---------------------------------------------------------------------
    def _create_frames(self) -> None:
        """Instantiate each UI page and store it in ``self.frames``.
        """
        for PageClass, name in [
            (DashboardPage, "Dashboard"),
            (ExerciseViewPage, "ExerciseView"),
            (SettingsPage, "Settings"),
        ]:
            frame = PageClass(parent=self.container, controller=self)
            self.frames[name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

    def show_frame(self, page_name: str) -> None:
        """Raise the requested page to the front.

        Parameters
        ----------
        page_name: str
            One of ``"Dashboard"``, ``"ExerciseView"`` or ``"Settings"``.
        """
        frame = self.frames.get(page_name)
        if not frame:
            raise ValueError(f"No page named {page_name} found in router.")
        frame.tkraise()

    # ---------------------------------------------------------------------
    # Sidebar UI
    # ---------------------------------------------------------------------
    def _populate_sidebar(self) -> None:
        """Create navigation buttons inside the sidebar.
        """
        # Title label
        title = ctk.CTkLabel(self.sidebar, text="Menu", font=("Helvetica", 16, "bold"))
        title.pack(pady=(20, 10))

        # Navigation buttons – each calls ``show_frame``.
        btn_cfg = dict(master=self.sidebar, width=180, corner_radius=6)
        btn_dashboard = ctk.CTkButton(**btn_cfg, text="Dashboard", command=lambda: self.show_frame("Dashboard"))
        btn_exercise = ctk.CTkButton(**btn_cfg, text="Exercises", command=lambda: self.show_frame("ExerciseView"))
        btn_settings = ctk.CTkButton(**btn_cfg, text="Settings", command=lambda: self.show_frame("Settings"))

        for btn in (btn_dashboard, btn_exercise, btn_settings):
            btn.pack(pady=10)

        # Footer – version info placeholder
        footer = ctk.CTkLabel(self.sidebar, text="v0.1", font=("Helvetica", 10))
        footer.pack(side="bottom", pady=10)


if __name__ == "__main__":
    app = App()
    app.mainloop()

# modules/dashboard/dashboard.py
"""Dashboard UI module for Programming Practices Platform.

Provides the main view displayed after successful login. Uses ttkbootstrap
widgets for a modern dark theme and includes placeholder widgets for
statistics, recent activity, and quick‑access buttons.
"""

import tkinter as tk
from ttkbootstrap import ttk

class DashboardView(ttk.Frame):
    """Main dashboard displayed after authentication.

    Args:
        master: The parent Tk widget (typically the root window).
    """

    def __init__(self, master: tk.Tk, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.configure(padding=20)
        self._create_widgets()

    def _create_widgets(self) -> None:
        """Create and layout dashboard widgets.

        The layout mirrors a modern cyber‑punk inspired UI with rounded
        cards and neon accent colours. All widgets are ttkbootstrap themed.
        """
        # Title label
        title = ttk.Label(
            self,
            text="Welcome to Programming Practices Platform",
            font=("Helvetica", 18, "bold"),
            bootstyle="primary"
        )
        title.pack(pady=(0, 15))

        # Statistics panel (placeholder)
        stats_frame = ttk.LabelFrame(self, text="Your Statistics", bootstyle="info")
        stats_frame.pack(fill="x", pady=5)
        ttk.Label(stats_frame, text="Quizzes Completed: 0", bootstyle="secondary").pack(anchor="w", padx=10, pady=2)
        ttk.Label(stats_frame, text="Challenges Solved: 0", bootstyle="secondary").pack(anchor="w", padx=10, pady=2)
        ttk.Label(stats_frame, text="Overall Score: 0%", bootstyle="secondary").pack(anchor="w", padx=10, pady=2)

        # Quick‑access buttons
        btn_frame = ttk.Frame(self)
        btn_frame.pack(fill="x", pady=10)
        ttk.Button(btn_frame, text="Start Quiz", bootstyle="success", width=15).grid(row=0, column=0, padx=5)
        ttk.Button(btn_frame, text="New Challenge", bootstyle="warning", width=15).grid(row=0, column=1, padx=5)
        ttk.Button(btn_frame, text="View Leaderboard", bootstyle="primary", width=15).grid(row=0, column=2, padx=5)

        # Recent activity panel (placeholder)
        activity_frame = ttk.LabelFrame(self, text="Recent Activity", bootstyle="light")
        activity_frame.pack(fill="both", expand=True, pady=5)
        ttk.Label(activity_frame, text="No activity yet.", bootstyle="secondary").pack(pady=20)

        # Add some spacing at the bottom
        ttk.Label(self, text="").pack(pady=5)

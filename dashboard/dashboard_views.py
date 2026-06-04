import customtkinter as ctk
from datetime import datetime
from dashboard.dashboard_controller import DashboardController
from core.theme_manager import ThemeManager
from utils.ui_helpers import create_stat_card, create_section_card
from core.logger import app_logger
from config.settings import APP_VERSION

class DashboardView(ctk.CTkFrame):
    def __init__(self, parent, app):
        super().__init__(parent, fg_color="#0C1324")
        self.app = app
        self.db = app.db
        self.controller = DashboardController(self.db)
        self.selected_module = "Dashboard"
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.build_layout()
        self.refresh()

    def build_layout(self):
        self.sidebar = ctk.CTkFrame(self, fg_color="#0F1220", corner_radius=0)
        self.sidebar.grid(row=0, column=0, sticky="nsew")
        self.sidebar.grid_rowconfigure(14, weight=1)

        title = ctk.CTkLabel(self.sidebar, text="Zyntriva SE Platform", font=ctk.CTkFont(size=20, weight="bold"), text_color="#FFFFFF")
        title.pack(padx=20, pady=(24, 4), anchor="w")
        ctk.CTkLabel(self.sidebar, text=APP_VERSION, font=ctk.CTkFont(size=11, weight="bold"), text_color="#38BDF8").pack(padx=20, pady=(0, 16), anchor="w")
        ctk.CTkLabel(self.sidebar, text="Programming Practices Platform", font=ctk.CTkFont(size=11), text_color="#8E9EC5").pack(padx=20, pady=(0, 24), anchor="w")

        self.nav_buttons = []
        nav_items = [
            ("Dashboard", "Platform Dashboard"),
            ("Process Models", "1. Process Models"),
            ("Version Control", "2. Version Control"),
            ("Refactoring", "3. Code Refactoring"),
            ("Testing", "4. Automated Testing"),
            ("Exception Lab", "5. Exception Handling"),
            ("Peer Review", "6. Peer Review"),
            ("Deployment", "7. Deployment Lifecycle"),
            ("Team Management", "8. Team & Outcomes"),
        ]
        for module_id, label in nav_items:
            button = ctk.CTkButton(
                self.sidebar,
                text=label,
                width=240,
                corner_radius=14,
                fg_color="#141D39" if module_id != self.selected_module else "#1F2937",
                hover_color="#1F2A53",
                command=lambda n=module_id: self.switch_module(n),
                anchor="w",
                text_color="#E2E8F0",
                font=ctk.CTkFont(size=13),
            )
            button.pack(fill="x", padx=16, pady=6)
            self.nav_buttons.append((module_id, button))

        self.settings_button = ctk.CTkButton(
            self.sidebar,
            text="User & SPI Settings",
            width=240,
            corner_radius=14,
            fg_color="#141D39",
            hover_color="#1F2A53",
            command=lambda: self.switch_module("User & SPI Settings"),
            anchor="w",
            text_color="#38BDF8",
            font=ctk.CTkFont(size=13, weight="bold"),
        )
        self.settings_button.pack(fill="x", padx=16, pady=(24, 0), side="bottom")

        ctk.CTkButton(
            self.sidebar,
            text="Logout",
            width=240,
            corner_radius=14,
            fg_color="#741F3A",
            hover_color="#8C2A4F",
            command=self.app.logout_user,
        ).pack(fill="x", padx=16, pady=(12, 24), side="bottom")

        self.update_nav_styles()

        content_area = ctk.CTkFrame(self, fg_color="#0C1324")
        content_area.grid(row=0, column=1, sticky="nsew", padx=(8, 8), pady=8)
        content_area.grid_rowconfigure(3, weight=1)
        content_area.grid_columnconfigure(0, weight=1)

        self.theme_mode = "dark"
        self.header_frame = ctk.CTkFrame(content_area, fg_color="#111A32", corner_radius=20)
        self.header_frame.grid(row=0, column=0, sticky="ew", padx=8, pady=8)
        self.header_frame.grid_columnconfigure(1, weight=1)

        self.welcome_label = ctk.CTkLabel(self.header_frame, text="Welcome back, Developer", font=ctk.CTkFont(size=22, weight="bold"), text_color="#FFFFFF")
        self.welcome_label.grid(row=0, column=0, sticky="w", padx=20, pady=(20, 5))

        self.profile_label = ctk.CTkLabel(self.header_frame, text="Explore your modules and practices.", text_color="#A2B0D8")
        self.profile_label.grid(row=1, column=0, sticky="w", padx=20, pady=(0, 20))

        button_frame = ctk.CTkFrame(self.header_frame, fg_color="#111A32", border_width=0)
        button_frame.grid(row=0, column=1, rowspan=2, sticky="ne", padx=20, pady=12)

        self.search_entry = ctk.CTkEntry(button_frame, placeholder_text="Search learning content...", width=260, corner_radius=14, fg_color="#131E3E")
        self.search_entry.grid(row=0, column=0, sticky="e", padx=(0, 10), pady=(0, 10))

        search_button = ctk.CTkButton(button_frame, text="Search", width=100, corner_radius=14, command=self.search_content)
        search_button.grid(row=1, column=0, sticky="e", padx=(0, 10), pady=(0, 10))

        theme_button = ctk.CTkButton(button_frame, text="Toggle Theme", width=140, corner_radius=14, command=self.toggle_theme)
        theme_button.grid(row=0, column=1, rowspan=2, sticky="e", pady=(0, 10))

        self.stats_frame = ctk.CTkFrame(content_area, fg_color="#111A32", corner_radius=20)
        self.stats_frame.grid(row=1, column=0, sticky="ew", padx=8, pady=8)
        self.stats_frame.grid_columnconfigure((0, 1, 2, 3), weight=1)

        self.module_title = ctk.CTkLabel(content_area, text="Dashboard Overview", font=ctk.CTkFont(size=20, weight="bold"), text_color="#FFFFFF")
        self.module_title.grid(row=2, column=0, sticky="w", padx=16, pady=(8, 0))

        self.module_frame = ctk.CTkScrollableFrame(content_area, fg_color="#0E172B", corner_radius=20, label_fg_color="#FFFFFF")
        self.module_frame.grid(row=3, column=0, sticky="nsew", padx=8, pady=8)
        self.module_frame.grid_columnconfigure(0, weight=1)

        self.side_panel = ctk.CTkFrame(self, fg_color="#101A2B", corner_radius=20)
        self.side_panel.grid(row=0, column=2, sticky="nsew", padx=(0, 8), pady=8)
        self.side_panel.grid_rowconfigure(6, weight=1)

        ctk.CTkLabel(self.side_panel, text="Notifications", font=ctk.CTkFont(size=16, weight="bold"), text_color="#FFFFFF").pack(anchor="w", padx=20, pady=(20, 10))
        self.notifications_container = ctk.CTkFrame(self.side_panel, fg_color="#0F1324", corner_radius=18)
        self.notifications_container.pack(fill="both", expand=False, padx=16, pady=(0, 12))

        ctk.CTkLabel(self.side_panel, text="Recent Activity", font=ctk.CTkFont(size=16, weight="bold"), text_color="#FFFFFF").pack(anchor="w", padx=20, pady=(12, 10))
        self.activity_container = ctk.CTkScrollableFrame(self.side_panel, fg_color="#0F1324", corner_radius=18, height=320, label_fg_color="#FFFFFF")
        self.activity_container.pack(fill="both", expand=True, padx=16, pady=(0, 20))

    def refresh(self):
        if self.app.current_user:
            self.welcome_label.configure(text=f"Welcome back, {self.app.current_user.get('full_name', 'Developer')}")
            self.profile_label.configure(text=f"Signed in as {self.app.current_user.get('username')}")
        self.update_stats()
        self.update_notifications()
        self.update_recent_activity()
        self.render_module(self.selected_module)

    def update_stats(self):
        for widget in self.stats_frame.winfo_children():
            widget.destroy()
        stats = self.controller.get_dashboard_stats()
        cards = [
            ("Commit History", stats.get("commits", 0)),
            ("Review Records", stats.get("reviews", 0)),
            ("Test Cases", stats.get("tests", 0)),
            ("Notifications", stats.get("notifications", 0)),
        ]
        for index, (title, value) in enumerate(cards):
            card = create_stat_card(self.stats_frame, title, str(value))
            card.grid(row=0, column=index, padx=10, pady=16, sticky="nsew")

    def update_notifications(self):
        for widget in self.notifications_container.winfo_children():
            widget.destroy()
        user_id = self.app.current_user.get("id") if self.app.current_user else 1
        notifications = self.controller.get_notifications(user_id)
        if not notifications:
            ctk.CTkLabel(self.notifications_container, text="No notifications yet.", text_color="#94A3B8").pack(padx=16, pady=16)
            return
        for note in notifications:
            card = ctk.CTkFrame(self.notifications_container, fg_color="#111A32", corner_radius=14)
            card.pack(fill="x", padx=12, pady=10)
            ctk.CTkLabel(card, text=note["title"], text_color="#FFFFFF", font=ctk.CTkFont(size=13, weight="bold")).pack(anchor="w", padx=14, pady=(12, 2))
            ctk.CTkLabel(card, text=note["message"], text_color="#B8C2DB", font=ctk.CTkFont(size=11), wraplength=240, justify="left").pack(anchor="w", padx=14, pady=(0, 12))

    def update_recent_activity(self):
        for widget in self.activity_container.winfo_children():
            widget.destroy()
        activities = self.controller.get_recent_activity()
        if not activities:
            ctk.CTkLabel(self.activity_container, text="No activity captured.", text_color="#94A3B8").pack(padx=16, pady=16)
            return
        for activity in activities:
            card = ctk.CTkFrame(self.activity_container, fg_color="#111A32", corner_radius=14)
            card.pack(fill="x", padx=12, pady=10)
            ctk.CTkLabel(card, text=activity["title"], text_color="#FFFFFF", font=ctk.CTkFont(size=13, weight="bold")).pack(anchor="w", padx=14, pady=(10, 2))
            ctk.CTkLabel(card, text=activity["message"], text_color="#BCC7E0", font=ctk.CTkFont(size=11), wraplength=240, justify="left").pack(anchor="w", padx=14, pady=(0, 2))
            ctk.CTkLabel(card, text=activity["created_at"].split("T")[0], text_color="#5B6A8B", font=ctk.CTkFont(size=10)).pack(anchor="w", padx=14, pady=(0, 12))

    def toggle_theme(self):
        self.theme_mode = ThemeManager.toggle_theme(self.theme_mode)
        app_logger.info(f"Theme switched to {self.theme_mode}")

    def clear_module(self):
        for widget in self.module_frame.winfo_children():
            widget.destroy()

    def switch_module(self, name: str):
        self.selected_module = name
        self.update_nav_styles()
        self.render_module(name)

    def update_nav_styles(self):
        for module_id, button in self.nav_buttons:
            button.configure(fg_color="#1F2937" if module_id == self.selected_module else "#141D39")
        self.settings_button.configure(fg_color="#1F2937" if self.selected_module == "User & SPI Settings" else "#141D39")

    def render_module(self, name: str):
        self.module_title.configure(text=name)
        self.clear_module()
        content = self.controller.load_module_data(name)
        create_section_card(self.module_frame, "Overview", content.get("overview", "" )).pack(fill="x", padx=16, pady=(12, 8))

        sections = content.get("sections", [])
        for section in sections:
            card = ctk.CTkFrame(self.module_frame, fg_color="#111A32", corner_radius=18, border_width=1, border_color="#27314D")
            card.pack(fill="x", padx=16, pady=8)
            ctk.CTkLabel(card, text=section.get("title", ""), font=ctk.CTkFont(size=15, weight="bold"), text_color="#FFFFFF").pack(anchor="w", padx=18, pady=(16, 6))
            ctk.CTkLabel(card, text=section.get("text", ""), wraplength=900, justify="left", text_color="#B1C2E8").pack(anchor="w", padx=18, pady=(0, 16))
            if section.get("list"):
                for item in section["list"]:
                    ctk.CTkLabel(card, text=f"• {item}", wraplength=900, justify="left", text_color="#C0D2F4").pack(anchor="w", padx=24, pady=2)

        if name == "Dashboard":
            self.render_commits()

    def render_commits(self):
        commits = self.controller.get_commits()
        card = ctk.CTkFrame(self.module_frame, fg_color="#111A32", corner_radius=18, border_width=1, border_color="#27314D")
        card.pack(fill="x", padx=16, pady=8)
        ctk.CTkLabel(card, text="Commit History", font=ctk.CTkFont(size=15, weight="bold"), text_color="#FFFFFF").pack(anchor="w", padx=18, pady=(16, 6))
        for commit in commits:
            commit_frame = ctk.CTkFrame(card, fg_color="#141F38", corner_radius=14)
            commit_frame.pack(fill="x", padx=18, pady=8)
            ctk.CTkLabel(commit_frame, text=commit["message"], font=ctk.CTkFont(size=13, weight="bold"), text_color="#F8FAFF").pack(anchor="w", padx=14, pady=(10, 0))
            ctk.CTkLabel(commit_frame, text=f"Branch: {commit['branch']} • Author: {commit['author']} • {commit['timestamp'].split('T')[0]}", font=ctk.CTkFont(size=11), text_color="#A5B2D1").pack(anchor="w", padx=14, pady=(4, 10))

    def search_content(self):
        query = self.search_entry.get().strip()
        if not query:
            self.module_title.configure(text="Dashboard")
            self.render_module("Dashboard")
            return
        items = self.controller.search_content(query)
        self.module_title.configure(text=f"Search Results for '{query}'")
        self.clear_module()
        if not items:
            ctk.CTkLabel(self.module_frame, text="No matching content found.", text_color="#94A3B8").pack(padx=16, pady=16)
            return
        for item in items:
            card = ctk.CTkFrame(self.module_frame, fg_color="#111A32", corner_radius=18)
            card.pack(fill="x", padx=16, pady=10)
            ctk.CTkLabel(card, text=item["title"], font=ctk.CTkFont(size=15, weight="bold"), text_color="#FFFFFF").pack(anchor="w", padx=18, pady=(16, 6))
            ctk.CTkLabel(card, text=item["description"], text_color="#B8C2DB", wraplength=900, justify="left").pack(anchor="w", padx=18, pady=(0, 16))

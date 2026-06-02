import customtkinter as ctk

class ThemeManager:
    DEFAULT_THEME = "dark-blue"
    FALLBACK_THEME = "blue"

    @staticmethod
    def apply_theme(mode: str = "dark"):
        ctk.set_appearance_mode(mode)
        try:
            ctk.set_default_color_theme(ThemeManager.DEFAULT_THEME)
        except Exception:
            try:
                ctk.set_default_color_theme(ThemeManager.FALLBACK_THEME)
            except Exception:
                # Last resort: use built-in theme defaults if customtkinter theme loading fails
                pass

    @staticmethod
    def toggle_theme(current_mode: str):
        if current_mode == "dark":
            ThemeManager.apply_theme("light")
            return "light"
        ThemeManager.apply_theme("dark")
        return "dark"

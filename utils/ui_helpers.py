import customtkinter as ctk


def create_stat_card(parent, title: str, value: str):
    card = ctk.CTkFrame(parent, fg_color="#141B2D", corner_radius=20, border_width=1, border_color="#2F3656")
    card.grid_columnconfigure(0, weight=1)
    ctk.CTkLabel(card, text=title, font=ctk.CTkFont(size=12), text_color="#9AA5C8").grid(row=0, column=0, sticky="w", padx=16, pady=(16, 4))
    ctk.CTkLabel(card, text=value, font=ctk.CTkFont(size=28, weight="bold"), text_color="#FFFFFF").grid(row=1, column=0, sticky="w", padx=16, pady=(0, 20))
    return card


def create_section_card(parent, heading: str, content: str):
    card = ctk.CTkFrame(parent, fg_color="#111827", corner_radius=18, border_width=1, border_color="#2C334A")
    ctk.CTkLabel(card, text=heading, font=ctk.CTkFont(size=14, weight="bold"), text_color="#FFFFFF").pack(anchor="w", padx=18, pady=(16, 6))
    ctk.CTkLabel(card, text=content, font=ctk.CTkFont(size=12), text_color="#B8C2DB", wraplength=520, justify="left").pack(anchor="w", padx=18, pady=(0, 16))
    return card

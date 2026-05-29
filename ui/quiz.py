import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox

class QuizScreen(ctk.CTkFrame):
    """Screen for MCQ quizzes.

    Displays a list of quizzes, shows selected question with options,
    lets the user submit an answer, and shows feedback.
    The `on_back` callback returns to the dashboard.
    """

    def __init__(self, master, on_back, **kwargs):
        super().__init__(master, **kwargs)
        self.master = master
        self.on_back = on_back
        self.configure(fg_color="#2B2B2B")
        self._build_ui()
        # Simple static quiz data; replace with DB query later
        self.quizzes = [
            {"question": "What is the output of print(2 ** 3)?",
             "options": ["6", "8", "9", "12"],
             "answer": "8"},
            {"question": "Which keyword is used to create a function in Python?",
             "options": ["def", "function", "func", "lambda"],
             "answer": "def"},
            {"question": "What does HTML stand for?",
             "options": ["Hyper Text Markup Language", "Home Tool Markup Language", "Hyperlinks and Text Markup Language", "Hyperlinking Textual Markup Language"],
             "answer": "Hyper Text Markup Language"},
        ]
        self.current_index = None

    def _build_ui(self):
        # Header with back button
        header = ctk.CTkFrame(self, fg_color="transparent")
        header.pack(fill="x", pady=5)
        ctk.CTkButton(header, text="← Back", command=self.on_back, width=80).pack(side="left", padx=10)
        ctk.CTkLabel(header, text="Quizzes", font=("Helvetica", 20, "bold"), text_color="#FFFFFF").pack(side="left", padx=20)

        # Main content area – split panels
        content = ctk.CTkFrame(self, fg_color="transparent")
        content.pack(fill="both", expand=True, padx=20, pady=10)

        # Left panel – list of quiz titles
        left_panel = ctk.CTkFrame(content, width=250, fg_color="#374151")
        left_panel.pack(side="left", fill="y")
        ctk.CTkLabel(left_panel, text="Quiz List", font=("Helvetica", 16), text_color="#E5E7EB").pack(pady=10)
        self.quiz_listbox = tk.Listbox(left_panel, bg="#1F2937", fg="#E5E7EB", selectbackground="#4B5563", highlightthickness=0, bd=0)
        self.quiz_listbox.pack(fill="both", expand=True, padx=5, pady=5)
        self.quiz_listbox.bind("<<ListboxSelect>>", self._load_quiz)
        self._populate_quiz_list()

        # Right panel – question and options
        right_panel = ctk.CTkFrame(content, fg_color="#1F2937")
        right_panel.pack(side="right", fill="both", expand=True, padx=10)
        self.question_label = ctk.CTkLabel(right_panel, text="Select a quiz", wraplength=400, font=("Helvetica", 16), text_color="#E5E7EB")
        self.question_label.pack(pady=10)
        self.var = tk.StringVar()
        self.option_buttons = []
        for i in range(4):
            rb = ctk.CTkRadioButton(right_panel, text="", variable=self.var, value=str(i), radiobutton_height=16, radiobutton_width=16)
            rb.pack(anchor="w", pady=5, padx=20)
            self.option_buttons.append(rb)
        btn_frame = ctk.CTkFrame(right_panel, fg_color="transparent")
        btn_frame.pack(pady=10)
        ctk.CTkButton(btn_frame, text="Submit Answer", command=self._submit_answer).grid(row=0, column=0, padx=5)

    def _populate_quiz_list(self):
        for idx, q in enumerate(self.quizzes):
            self.quiz_listbox.insert(tk.END, f"Quiz {idx + 1}")

    def _load_quiz(self, event):
        selection = self.quiz_listbox.curselection()
        if not selection:
            return
        self.current_index = selection[0]
        quiz = self.quizzes[self.current_index]
        self.question_label.configure(text=quiz["question"])
        for i, opt in enumerate(quiz["options"]):
            self.option_buttons[i].configure(text=opt, value=opt)
        self.var.set("")

    def _submit_answer(self):
        if self.current_index is None:
            messagebox.showwarning("No quiz selected", "Please select a quiz first.")
            return
        selected = self.var.get()
        if not selected:
            messagebox.showwarning("No answer", "Please choose an option.")
            return
        correct = self.quizzes[self.current_index]["answer"]
        if selected == correct:
            messagebox.showinfo("Result", "Correct! 🎉")
        else:
            messagebox.showinfo("Result", f"Incorrect. Correct answer: {correct}")

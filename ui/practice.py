import customtkinter as ctk
import tkinter as tk
from tkinter import scrolledtext

class PracticeScreen(ctk.CTkFrame):
    """Screen for coding practice exercises.

    Shows a list of exercises on the left, a code editor on the right, and
    Run / Submit buttons. The `on_back` callback returns to the dashboard.
    """

    def __init__(self, master, on_back, **kwargs):
        super().__init__(master, **kwargs)
        self.master = master
        self.on_back = on_back
        self.configure(fg_color="#2B2B2B")
        self._build_ui()

    def _build_ui(self):
        # Header with back button
        header = ctk.CTkFrame(self, fg_color="transparent")
        header.pack(fill="x", pady=5)
        ctk.CTkButton(header, text="← Back", command=self.on_back, width=80).pack(side="left", padx=10)
        ctk.CTkLabel(header, text="Practice Exercises", font=("Helvetica", 20, "bold"), text_color="#FFFFFF").pack(side="left", padx=20)

        # Main content area – split panels
        content = ctk.CTkFrame(self, fg_color="transparent")
        content.pack(fill="both", expand=True, padx=20, pady=10)

        # Left panel – list of exercises
        left_panel = ctk.CTkFrame(content, width=250, fg_color="#374151")
        left_panel.pack(side="left", fill="y")
        ctk.CTkLabel(left_panel, text="Exercises", font=("Helvetica", 16), text_color="#E5E7EB").pack(pady=10)
        self.exercise_listbox = tk.Listbox(left_panel, bg="#1F2937", fg="#E5E7EB", selectbackground="#4B5563", highlightthickness=0, bd=0)
        self.exercise_listbox.pack(fill="both", expand=True, padx=5, pady=5)
        self.exercise_listbox.bind("<<ListboxSelect>>", self._load_exercise)
        self._populate_exercises()

        # Right panel – code editor and controls
        right_panel = ctk.CTkFrame(content, fg_color="#1F2937")
        right_panel.pack(side="right", fill="both", expand=True, padx=10)
        ctk.CTkLabel(right_panel, text="Code Editor", font=("Helvetica", 16), text_color="#E5E7EB").pack(pady=5)
        self.editor = scrolledtext.ScrolledText(right_panel, wrap="none", font=("Consolas", 12), bg="#111827", fg="#E5E7EB", insertbackground="#E5E7EB")
        self.editor.pack(fill="both", expand=True, padx=5, pady=5)

        # Run / Submit buttons
        btn_frame = ctk.CTkFrame(right_panel, fg_color="transparent")
        btn_frame.pack(pady=5)
        ctk.CTkButton(btn_frame, text="Run", command=self._run_code, width=100).grid(row=0, column=0, padx=5)
        ctk.CTkButton(btn_frame, text="Clear", command=self._clear_editor, width=100).grid(row=0, column=1, padx=5)

        # Output area
        ctk.CTkLabel(right_panel, text="Output", font=("Helvetica", 16), text_color="#E5E7EB").pack(pady=5)
        self.output = scrolledtext.ScrolledText(right_panel, height=8, wrap="word", font=("Consolas", 11), bg="#111827", fg="#10B981", insertbackground="#10B981", state="disabled")
        self.output.pack(fill="both", expand=False, padx=5, pady=5)

    def _populate_exercises(self):
        # In a real app, this would query the DB. Here we use static examples.
        exercises = [
            "Hello World",
            "Factorial (Recursion)",
            "Palindrome Checker",
            "Fibonacci Sequence",
            "Prime Numbers",
        ]
        for ex in exercises:
            self.exercise_listbox.insert(tk.END, ex)

    def _load_exercise(self, event):
        # Load a starter template for the selected exercise.
        selection = self.exercise_listbox.curselection()
        if not selection:
            return
        idx = selection[0]
        name = self.exercise_listbox.get(idx)
        templates = {
            "Hello World": "print('Hello, World!')",
            "Factorial (Recursion)": "def fact(n):\n    return 1 if n == 0 else n * fact(n-1)\n\nprint(fact(5))",
            "Palindrome Checker": "def is_palindrome(s):\n    return s == s[::-1]\n\nprint(is_palindrome('radar'))",
            "Fibonacci Sequence": "def fib(n):\n    a, b = 0, 1\n    for _ in range(n):\n        a, b = b, a + b\n    return a\n\nprint([fib(i) for i in range(10)])",
            "Prime Numbers": "def is_prime(n):\n    if n < 2:
        return False\n    for i in range(2, int(n**0.5) + 1):\n        if n % i == 0:
            return False\n    return True\n\nprint([i for i in range(2, 30) if is_prime(i)])",
        }
        self.editor.delete('1.0', tk.END)
        self.editor.insert(tk.END, templates.get(name, ""))
        self._clear_output()

    def _clear_editor(self):
        self.editor.delete('1.0', tk.END)
        self._clear_output()

    def _clear_output(self):
        self.output.configure(state="normal")
        self.output.delete('1.0', tk.END)
        self.output.configure(state="disabled")

    def _run_code(self):
        code = self.editor.get('1.0', tk.END)
        # Execute code in a restricted namespace
        local_vars = {}
        try:
            exec(code, {}, local_vars)
            output = "Executed successfully."
        except Exception as e:
            output = f"Error: {e}"
        self.output.configure(state="normal")
        self.output.delete('1.0', tk.END)
        self.output.insert(tk.END, output)
        self.output.configure(state="disabled")

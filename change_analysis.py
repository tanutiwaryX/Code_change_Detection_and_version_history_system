
import tkinter as tk
from tkinter import messagebox
import os
import difflib

def change_analysis(window):
    win = tk.Toplevel(window)
    win.title("Change Analysis | Code Tracker")
    win.geometry("900x700")
    win.configure(bg="#F4F0FF")

    # Header
    tk.Label(
        win, text="</>  Change Analysis",
        font=("Arial", 22, "bold"),
        bg="#36245D", fg="white", pady=20
    ).pack(fill="x")

    # Version inputs
    for text in ["First Version", "Second Version"]:
        tk.Label(
            win, text=text,
            font=("Arial", 11, "bold"),
            bg="#F4F0FF", fg="#21183F"
        ).pack(pady=(15, 3))

        entry = tk.Entry(
            win, width=25, font=("Arial", 11), relief="flat"
        )
        entry.pack(ipady=6, pady=3)

        if text == "First Version":
            v1 = entry
        else:
            v2 = entry

    # Analysis result
    result = tk.Label(
        win, text="Enter two versions to analyze",
        font=("Arial", 12), bg="#FFFFFF", fg="#21183F",
        width=42, height=9, justify="left",
        padx=15, relief="solid", bd=1
    )
    result.pack(pady=20)

    def analyze():
        first = v1.get().strip()
        second = v2.get().strip()

        if not first or not second:
            messagebox.showwarning(
                "Warning", "Enter both version numbers.", parent=win
            )
            return

        file1 = os.path.join("versions", f"version{first}.txt")
        file2 = os.path.join("versions", f"version{second}.txt")

        if not os.path.isfile(file1) or not os.path.isfile(file2):
            messagebox.showerror(
                "Error", "Version not found.", parent=win
            )
            return

        try:
            with open(file1, encoding="utf-8") as f:
                code1 = f.readlines()

            with open(file2, encoding="utf-8") as f:
                code2 = f.readlines()

            added = deleted = same = 0

            for line in difflib.ndiff(code1, code2):
                if line.startswith("+ "):
                    added += 1
                elif line.startswith("- "):
                    deleted += 1
                elif line.startswith("  "):
                    same += 1

            result.config(
                text=f"VERSION {first}  →  VERSION {second}\n\n"
                     f"Added Lines       : {added}\n\n"
                     f"Deleted Lines     : {deleted}\n\n"
                     f"Unchanged Lines   : {same}\n\n"
                     f"Total Changes     : {added + deleted}"
            )

        except OSError as e:
            messagebox.showerror("File Error", str(e), parent=win)

    # Analyze button
    tk.Button(
        win, text="ANALYZE CHANGES  →",
        font=("Arial", 11, "bold"),
        bg="#7654E8", fg="white",
        activebackground="#6040CE",
        activeforeground="white",
        relief="flat", cursor="hand2",
        padx=20, pady=9, command=analyze
    ).pack(pady=(0, 15))

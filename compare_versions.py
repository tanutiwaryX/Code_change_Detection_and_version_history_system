
import tkinter as tk
from tkinter import messagebox
import os
import difflib

def compare_versions(window):
    win = tk.Toplevel(window)
    win.title("Compare Versions | Code Tracker")
    win.geometry("900x700")
    win.configure(bg="#F4F0FF")

    # Header
    tk.Label(
        win, text="</>  Compare Versions",
        font=("Arial", 22, "bold"),
        bg="#36245D", fg="white", pady=20
    ).pack(fill="x")

    # Version selection
    frame = tk.Frame(win, bg="#F4F0FF")
    frame.pack(pady=20)

    for col, text in enumerate(["First Version", "Second Version"]):
        tk.Label(
            frame, text=text,
            font=("Arial", 11, "bold"),
            bg="#F4F0FF", fg="#21183F"
        ).grid(row=0, column=col, padx=15)

    v1 = tk.Entry(frame, width=25, font=("Arial", 11), relief="flat")
    v1.grid(row=1, column=0, padx=15, pady=8, ipady=6)

    v2 = tk.Entry(frame, width=25, font=("Arial", 11), relief="flat")
    v2.grid(row=1, column=1, padx=15, pady=8, ipady=6)

    # Comparison output
    result = tk.Text(
        win, font=("Consolas", 10),
        bg="#21183F", fg="#E9DFFF",
        insertbackground="white", relief="flat",
        wrap="none"
    )
    result.pack(fill="both", expand=True, padx=25, pady=10)

    result.tag_config("added", foreground="#6EE7B7")
    result.tag_config("deleted", foreground="#FDA4AF")
    result.tag_config("same", foreground="#E9DFFF")

    def compare():
        first = v1.get().strip()
        second = v2.get().strip()

        if not first or not second:
            messagebox.showwarning(
                "Missing Version", "Enter both version numbers.", parent=win
            )
            return

        file1 = os.path.join("versions", f"version{first}.txt")
        file2 = os.path.join("versions", f"version{second}.txt")

        if not os.path.isfile(file1) or not os.path.isfile(file2):
            messagebox.showerror(
                "Error", "Version not found. Check the version numbers.",
                parent=win
            )
            return

        try:
            with open(file1, encoding="utf-8") as f:
                code1 = f.readlines()

            with open(file2, encoding="utf-8") as f:
                code2 = f.readlines()

            result.delete("1.0", tk.END)

            for line in difflib.ndiff(code1, code2):
                if line.startswith("+ "):
                    result.insert(tk.END, "ADDED    " + line[2:], "added")
                elif line.startswith("- "):
                    result.insert(tk.END, "DELETED  " + line[2:], "deleted")
                elif line.startswith("  "):
                    result.insert(tk.END, "SAME     " + line[2:], "same")

        except OSError as e:
            messagebox.showerror("File Error", str(e), parent=win)

    # Compare button
    tk.Button(
        win, text="COMPARE VERSIONS  →",
        font=("Arial", 11, "bold"),
        bg="#7654E8", fg="white",
        activebackground="#6040CE",
        activeforeground="white",
        relief="flat", cursor="hand2",
        padx=20, pady=10,
        command=compare
    ).pack(pady=(5, 15))

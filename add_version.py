
import tkinter as tk
from tkinter import messagebox
import os

def add_version(window):
    win = tk.Toplevel(window)
    win.title("Add New Version | Code Tracker")
    win.geometry("900x700")
    win.configure(bg="#F4F0FF")

    # Header
    tk.Label(
        win, text="</>  Add New Version",
        font=("Arial", 22, "bold"),
        bg="#36245D", fg="white", pady=20
    ).pack(fill="x")

    # Version number
    tk.Label(
        win, text="Version Number",
        font=("Arial", 11, "bold"),
        bg="#F4F0FF", fg="#21183F"
    ).pack(anchor="w", padx=25, pady=(20, 5))

    version = tk.Entry(win, font=("Arial", 12), relief="flat")
    version.pack(fill="x", padx=25, ipady=8)

    # Code editor
    tk.Label(
        win, text="Paste Your Code",
        font=("Arial", 11, "bold"),
        bg="#F4F0FF", fg="#21183F"
    ).pack(anchor="w", padx=25, pady=(15, 5))

    code_frame = tk.Frame(win, bg="#21183F", padx=3, pady=3)
    code_frame.pack(fill="both", expand=True, padx=25, pady=5)

    code = tk.Text(
        code_frame, font=("Consolas", 11),
        bg="#21183F", fg="#E9DFFF",
        insertbackground="white", relief="flat",
        wrap="none", undo=True
    )
    code.pack(fill="both", expand=True)

    # Save version
    def save():
        v = version.get().strip()
        text = code.get("1.0", "end-1c").strip()

        if not v or not text:
            messagebox.showwarning(
                "Warning", "Enter version number and code.", parent=win
            )
            return

        if any(c in v for c in r'\/:*?"<>|'):
            messagebox.showwarning(
                "Invalid Version", "Enter a valid version number.", parent=win
            )
            return

        os.makedirs("versions", exist_ok=True)

        try:
            with open(f"versions/version{v}.txt", "w", encoding="utf-8") as f:
                f.write(text)

            messagebox.showinfo(
                "Success", f"Version {v} saved successfully!", parent=win
            )
            win.destroy()
        except OSError as e:
            messagebox.showerror("Error", str(e), parent=win)

    # Save button
    tk.Button(
        win, text="SAVE VERSION  →",
        font=("Arial", 11, "bold"),
        bg="#7654E8", fg="white",
        activebackground="#6040CE",
        activeforeground="white",
        relief="flat", cursor="hand2",
        padx=10, pady=5,
        command=save
    ).pack(anchor="e", padx=25, pady=15)

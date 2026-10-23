
import tkinter as tk
import os

def version_history(window):
    win = tk.Toplevel(window)
    win.title("Version History | Code Tracker")
    win.geometry("900x700")
    win.configure(bg="#F4F0FF")

    # Header
    tk.Label(
        win, text="</>  Version History",
        font=("Arial", 22, "bold"),
        bg="#36245D", fg="white", pady=20
    ).pack(fill="x")

    tk.Label(
        win, text="Select a version to view its code",
        font=("Arial", 11),
        bg="#F4F0FF", fg="#817795"
    ).pack(anchor="w", padx=25, pady=(20, 10))

    # Version list
    versions = tk.Listbox(
        win, height=7, font=("Arial", 11),
        bg="white", fg="#21183F",
        selectbackground="#7654E8",
        selectforeground="white",
        relief="flat", highlightthickness=1,
        highlightbackground="#DDD2FA"
    )
    versions.pack(fill="x", padx=25)

    # Code viewer
    tk.Label(
        win, text="Source Code",
        font=("Arial", 11, "bold"),
        bg="#F4F0FF", fg="#21183F"
    ).pack(anchor="w", padx=25, pady=(15, 5))

    code_frame = tk.Frame(win, bg="#21183F", padx=3, pady=3)
    code_frame.pack(fill="both", expand=True, padx=25, pady=(0, 20))

    code = tk.Text(
        code_frame, font=("Consolas", 10),
        bg="#21183F", fg="#E9DFFF",
        insertbackground="white",
        relief="flat", wrap="none"
    )
    code.pack(fill="both", expand=True)

    # Load saved versions
    if os.path.exists("versions"):
        for file in sorted(os.listdir("versions")):
            if file.endswith(".txt"):
                versions.insert(tk.END, file)

    def show_code(event):
        selected = versions.curselection()
        if not selected:
            return

        file = versions.get(selected[0])
        try:
            with open(os.path.join("versions", file),
                      "r", encoding="utf-8") as f:
                data = f.read()

            code.delete("1.0", tk.END)
            code.insert("1.0", data)
        except OSError as e:
            code.delete("1.0", tk.END)
            code.insert("1.0", f"Unable to open file:\n{e}")

    versions.bind("<<ListboxSelect>>", show_code)

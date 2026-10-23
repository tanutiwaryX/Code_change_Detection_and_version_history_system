
import tkinter as tk
from tkinter import messagebox

from add_version import add_version
from version_history import version_history
from compare_versions import compare_versions
from change_analysis import change_analysis

window = tk.Tk()
window.title("Code Tracker | Developer Dashboard")
window.geometry("1150x720")
window.minsize(950, 650)
window.configure(bg="#F4F0FF")

BG = "#F4F0FF"
DARK = "#21183F"
PURPLE = "#7654E8"
WHITE = "#FFFFFF"
MUTED = "#817795"

# LEFT SIDEBAR
sidebar = tk.Frame(window, bg=DARK, width=265)
sidebar.pack(side="left", fill="y")
sidebar.pack_propagate(False)

tk.Label(sidebar, text="</>", font=("Arial", 38, "bold"),
         bg=DARK, fg="#B7A0FF").pack(anchor="w", padx=28, pady=(55, 10))

tk.Label(sidebar, text="CODE TRACKER", font=("Arial", 17, "bold"),
         bg=DARK, fg=WHITE).pack(anchor="w", padx=22, pady=5)

tk.Label(sidebar, text="DEVELOPER WORKSPACE", font=("Arial", 10),
         bg=DARK, fg="#B7A0FF").pack(anchor="w", padx=22, pady=15)

tk.Frame(sidebar, bg="#493B68", height=1).pack(
    fill="x", padx=18, pady=25
)

tk.Label(sidebar, text="■  Dashboard", font=("Arial", 12, "bold"),
         bg="#3D2D61", fg=WHITE, anchor="w",
         padx=20, pady=18).pack(fill="x", padx=5, pady=5)

tk.Label(sidebar, text="✦  Version Control", font=("Arial", 12),
         bg=DARK, fg="#C9BDF0", anchor="w",
         padx=22, pady=18).pack(fill="x")

tk.Label(sidebar, text="⚙  Code Analysis", font=("Arial", 12),
         bg=DARK, fg="#C9BDF0", anchor="w",
         padx=22, pady=18).pack(fill="x")

tk.Label(sidebar, text="YOUR CODE.\nYOUR HISTORY.\nYOUR CONTROL.",
         font=("Arial", 13, "bold"), bg=DARK,
         fg="#B7A0FF", justify="left").pack(
             side="bottom", anchor="w", padx=25, pady=30
         )

# MAIN AREA
main = tk.Frame(window, bg=BG)
main.pack(side="left", fill="both", expand=True, padx=25, pady=20)

# TOP BAR
topbar = tk.Frame(main, bg=BG)
topbar.pack(fill="x", pady=(0, 15))

tk.Label(topbar, text="DEVELOPER DASHBOARD",
         bg=BG, fg=MUTED).pack(side="left")

tk.Button(
    topbar, text="✕ EXIT", bg="#D94F68", fg=WHITE,
    font=("Arial", 10, "bold"), relief="flat",
    cursor="hand2",
    command=lambda: (
        window.destroy() if messagebox.askyesno(
            "Exit", "Do you want to exit Code Tracker?"
        ) else None
    )
).pack(side="right", padx=5)

tk.Label(topbar, text="● SYSTEM READY", bg="#DDF8EE",
         fg="#16866F", font=("Arial", 10, "bold"),
         padx=12, pady=9).pack(side="right", padx=8)

# WELCOME BANNER
hero = tk.Frame(main, bg="#36245D", padx=20, pady=25)
hero.pack(fill="x")

tk.Label(hero, text="Welcome to Code Tracker ✦",
         font=("Arial", 23, "bold"),
         bg="#36245D", fg=WHITE).pack(anchor="w")

tk.Label(hero, text="Manage versions. Compare code. Understand every change.",
         bg="#36245D", fg="#D7C9FF").pack(anchor="w", pady=8)

# PROJECT INFORMATION
info = tk.Frame(main, bg=BG)
info.pack(fill="x", pady=15)

for title, value, color in [
    ("PROJECT", "Code Tracker", PURPLE),
    ("CORE TOOLS", "04 Features", "#159E96"),
    ("PLATFORM", "Python + Tkinter", "#D9912B")
]:
    box = tk.Frame(info, bg=WHITE, padx=12, pady=12)
    box.pack(side="left", expand=True, fill="x", padx=4)

    tk.Label(box, text=title, bg=WHITE, fg=MUTED).pack(anchor="w")
    tk.Label(box, text=value, bg=WHITE, fg=color,
             font=("Arial", 12, "bold")).pack(anchor="w", pady=5)

# WORKSPACE
tk.Label(main, text="Workspace Tools", font=("Arial", 18, "bold"),
         bg=BG, fg=DARK).pack(anchor="w")

tk.Label(main, text="Choose a tool to get started",
         bg=BG, fg=MUTED).pack(anchor="w", pady=5)

tools_frame = tk.Frame(main, bg=BG)
tools_frame.pack(fill="both", expand=True, pady=10)

tools = [
    ("01", "Add New Version", "Save a new code version",
     PURPLE, add_version),
    ("02", "Version History", "Browse saved versions",
     "#159E96", version_history),
    ("03", "Compare Versions", "Find code differences",
     "#D9912B", compare_versions),
    ("04", "Change Analysis", "Examine code changes",
     "#A64DCC", change_analysis)
]

for i, (num, title, desc, color, func) in enumerate(tools):
    card = tk.Frame(tools_frame, bg=WHITE, padx=15, pady=12)
    card.grid(row=i // 2, column=i % 2,
              sticky="nsew", padx=5, pady=5)

    tk.Label(card, text=num, bg="#F0E9FF", fg=color,
             font=("Arial", 12, "bold"),
             padx=10, pady=5).pack(anchor="w")

    tk.Label(card, text=title, bg=WHITE, fg=DARK,
             font=("Arial", 12, "bold")).pack(anchor="w", pady=6)

    tk.Label(card, text=desc, bg=WHITE,
             fg=MUTED).pack(anchor="w")

    tk.Button(card, text="Open Tool →", bg=color, fg=WHITE,
              relief="flat", cursor="hand2",
              command=lambda f=func: f(window)).pack(
                  anchor="w", pady=6
              )

tools_frame.grid_columnconfigure(0, weight=1)
tools_frame.grid_columnconfigure(1, weight=1)
tools_frame.grid_rowconfigure(0, weight=1)
tools_frame.grid_rowconfigure(1, weight=1)

window.mainloop()

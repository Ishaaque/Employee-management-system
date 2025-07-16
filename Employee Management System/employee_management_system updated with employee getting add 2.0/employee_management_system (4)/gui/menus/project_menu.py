import tkinter as tk
from tkinter import messagebox
from gui.project_gui import assign_project_gui, view_projects_gui, update_project_gui, remove_project_gui

def open_project_menu():
    window = tk.Tk()
    window.title("Project Management Menu")
    window.geometry("500x400")
    window.configure(bg="#f4f4f4")

    tk.Label(window, text="Project Management", font=("Arial", 20, "bold"), bg="#f4f4f4").pack(pady=20)

    tk.Button(window, text="Assign Project", font=("Arial", 14), width=25, bg="#add8e6", command=assign_project_gui).pack(pady=10)
    tk.Button(window, text="View Assigned Projects", font=("Arial", 14), width=25, bg="#90ee90", command=view_projects_gui).pack(pady=10)
    tk.Button(window, text="Update Project Assignment", font=("Arial", 14), width=25, bg="#ffd700", command=update_project_gui).pack(pady=10)
    tk.Button(window, text="Remove Project", font=("Arial", 14), width=25, bg="#ff7f7f", command=remove_project_gui).pack(pady=10)

    tk.Button(window, text="Back to Main Menu", font=("Arial", 14), width=25, bg="#d3d3d3", command=window.destroy).pack(pady=20)

    window.mainloop()

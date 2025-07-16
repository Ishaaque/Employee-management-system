import tkinter as tk
from tkinter import messagebox
from gui.performance_gui import add_performance_gui, view_performance_gui, update_performance_gui, delete_performance_gui

def open_performance_menu():
    window = tk.Tk()
    window.title("Performance Management Menu")
    window.geometry("500x400")
    window.configure(bg="#ffffff")

    tk.Label(window, text="Performance Management", font=("Arial", 20, "bold"), bg="#ffffff").pack(pady=20)

    tk.Button(window, text="Add Performance Record", font=("Arial", 14), width=30, bg="#add8e6", command=add_performance_gui).pack(pady=10)
    tk.Button(window, text="View Performance", font=("Arial", 14), width=30, bg="#90ee90", command=view_performance_gui).pack(pady=10)
    tk.Button(window, text="Update Performance", font=("Arial", 14), width=30, bg="#ffd700", command=update_performance_gui).pack(pady=10)
    tk.Button(window, text="Delete Performance Record", font=("Arial", 14), width=30, bg="#ff7f7f", command=delete_performance_gui).pack(pady=10)

    tk.Button(window, text="Back to Main Menu", font=("Arial", 14), width=30, bg="#d3d3d3", command=window.destroy).pack(pady=20)

    window.mainloop()

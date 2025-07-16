import tkinter as tk
from tkinter import messagebox
from gui.leave_gui import apply_leave_gui, view_leaves_gui, approve_leave_gui, reject_leave_gui

def open_leave_menu():
    window = tk.Tk()
    window.title("Leave Management Menu")
    window.geometry("500x400")
    window.configure(bg="#f8f8ff")

    tk.Label(window, text="Leave Management", font=("Arial", 20, "bold"), bg="#f8f8ff").pack(pady=20)

    tk.Button(window, text="Apply Leave", font=("Arial", 14), width=25, bg="#add8e6", command=apply_leave_gui).pack(pady=10)
    tk.Button(window, text="View All Leaves", font=("Arial", 14), width=25, bg="#90ee90", command=view_leaves_gui).pack(pady=10)
    tk.Button(window, text="Approve Leave", font=("Arial", 14), width=25, bg="#ffd700", command=approve_leave_gui).pack(pady=10)
    tk.Button(window, text="Reject Leave", font=("Arial", 14), width=25, bg="#ff7f7f", command=reject_leave_gui).pack(pady=10)

    tk.Button(window, text="Back to Main Menu", font=("Arial", 14), width=25, bg="#d3d3d3", command=window.destroy).pack(pady=20)

    window.mainloop()

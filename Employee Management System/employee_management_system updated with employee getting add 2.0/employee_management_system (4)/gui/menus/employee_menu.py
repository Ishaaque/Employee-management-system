import tkinter as tk
from tkinter import messagebox
from gui.employee_gui import add_employee_gui, view_employees_gui, update_employee_gui, delete_employee_gui

def open_employee_menu():
    window = tk.Toplevel()
    window.title("Employee Menu")
    window.geometry("400x400")
    window.configure(bg="#e0f7fa")

    tk.Label(window, text="Employee Menu", font=("Arial", 18, "bold"), bg="#e0f7fa").pack(pady=20)

    tk.Button(window, text="Add Employee", font=("Arial", 14), width=25, bg="#4caf50", fg="white",
              command=add_employee_gui).pack(pady=10)

    tk.Button(window, text="View Employees", font=("Arial", 14), width=25, bg="#2196f3", fg="white",
              command=view_employees_gui).pack(pady=10)

    tk.Button(window, text="Update Employee", font=("Arial", 14), width=25, bg="#ff9800", fg="white",
              command=update_employee_gui).pack(pady=10)

    tk.Button(window, text="Delete Employee", font=("Arial", 14), width=25, bg="#f44336", fg="white",
              command=delete_employee_gui).pack(pady=10)

    tk.Button(window, text="Back to Dashboard", font=("Arial", 12), width=20, bg="#9e9e9e", fg="white",
              command=window.destroy).pack(pady=20)

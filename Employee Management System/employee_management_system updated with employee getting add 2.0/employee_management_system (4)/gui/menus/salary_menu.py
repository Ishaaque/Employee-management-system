import tkinter as tk
from tkinter import messagebox
from gui.salary_gui import calculate_salary_gui, view_salary_gui, update_salary_gui, delete_salary_gui

def open_salary_menu():
    window = tk.Tk()
    window.title("Salary Management Menu")
    window.geometry("500x400")
    window.configure(bg="#fefefe")

    tk.Label(window, text="Salary Management", font=("Arial", 20, "bold"), bg="#fefefe").pack(pady=20)

    tk.Button(window, text="Calculate Salary", font=("Arial", 14), width=30, bg="#add8e6", command=calculate_salary_gui).pack(pady=10)
    tk.Button(window, text="View Salaries", font=("Arial", 14), width=30, bg="#90ee90", command=view_salary_gui).pack(pady=10)
    tk.Button(window, text="Update Salary Record", font=("Arial", 14), width=30, bg="#ffd700", command=update_salary_gui).pack(pady=10)
    tk.Button(window, text="Delete Salary Record", font=("Arial", 14), width=30, bg="#ff7f7f", command=delete_salary_gui).pack(pady=10)

    tk.Button(window, text="Back to Main Menu", font=("Arial", 14), width=30, bg="#d3d3d3", command=window.destroy).pack(pady=20)

    window.mainloop()

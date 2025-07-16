import tkinter as tk
from tkinter import messagebox
from gui.department_gui import add_department_gui, view_departments_gui, update_department_gui, delete_department_gui

def open_department_menu():
    window = tk.Tk()
    window.title("Department Management Menu")
    window.geometry("500x400")
    window.configure(bg="#f0f0f0")

    tk.Label(window, text="Department Management", font=("Arial", 20, "bold"), bg="#f0f0f0").pack(pady=20)

    tk.Button(window, text="Add Department", font=("Arial", 14), width=25, bg="#add8e6", command=add_department_gui).pack(pady=10)
    tk.Button(window, text="View Departments", font=("Arial", 14), width=25, bg="#90ee90", command=view_departments_gui).pack(pady=10)
    tk.Button(window, text="Update Department", font=("Arial", 14), width=25, bg="#ffd700", command=update_department_gui).pack(pady=10)
    tk.Button(window, text="Delete Department", font=("Arial", 14), width=25, bg="#ff7f7f", command=delete_department_gui).pack(pady=10)
    
    tk.Button(window, text="Back to Main Menu", font=("Arial", 14), width=25, bg="#d3d3d3", command=window.destroy).pack(pady=20)

    window.mainloop()

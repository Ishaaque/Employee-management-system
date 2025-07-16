import sys
import os
import tkinter as tk

# Add the project root directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..")))

from gui.menus.employee_menu import open_employee_menu
from gui.menus.department_menu import open_department_menu
from gui.menus.attendance_menu import open_attendance_menu
from gui.menus.leave_menu import open_leave_menu
from gui.menus.salary_menu import open_salary_menu
from gui.menus.project_menu import open_project_menu
from gui.menus.performance_menu import open_performance_menu

def open_main_dashboard(user_id, user_name, role):
    dashboard = tk.Tk()
    dashboard.title("Employee Management System")
    dashboard.geometry("600x400")

    tk.Label(dashboard, text=f"Welcome, {user_name}", font=("Arial", 18)).pack(pady=10)

    btn_frame = tk.Frame(dashboard)
    btn_frame.pack(pady=20)

    tk.Button(btn_frame, text="Employee Management", width=25, command=open_employee_menu).grid(row=0, column=0, padx=10, pady=5)
    tk.Button(btn_frame, text="Department Management", width=25, command=open_department_menu).grid(row=1, column=0, padx=10, pady=5)
    tk.Button(btn_frame, text="Attendance", width=25, command=open_attendance_menu).grid(row=2, column=0, padx=10, pady=5)
    tk.Button(btn_frame, text="Leave Requests", width=25, command=open_leave_menu).grid(row=3, column=0, padx=10, pady=5)
    tk.Button(btn_frame, text="Salary Report", width=25, command=open_salary_menu).grid(row=4, column=0, padx=10, pady=5)
    tk.Button(btn_frame, text="Projects", width=25, command=open_project_menu).grid(row=5, column=0, padx=10, pady=5)
    tk.Button(btn_frame, text="Performance Reviews", width=25, command=open_performance_menu).grid(row=6, column=0, padx=10, pady=5)

    dashboard.mainloop()

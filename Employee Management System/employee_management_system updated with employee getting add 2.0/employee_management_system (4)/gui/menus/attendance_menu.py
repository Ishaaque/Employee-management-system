import tkinter as tk
from tkinter import messagebox
from gui.attendance_gui import mark_attendance_gui, view_attendance_gui, update_attendance_gui, delete_attendance_gui

def open_attendance_menu():
    window = tk.Tk()
    window.title("Attendance Management Menu")
    window.geometry("500x400")
    window.configure(bg="#ffffff")

    tk.Label(window, text="Attendance Management", font=("Arial", 20, "bold"), bg="#ffffff").pack(pady=20)

    tk.Button(window, text="Mark Attendance", font=("Arial", 14), width=30, bg="#add8e6", command=mark_attendance_gui).pack(pady=10)
    tk.Button(window, text="View Attendance Records", font=("Arial", 14), width=30, bg="#90ee90", command=view_attendance_gui).pack(pady=10)
    tk.Button(window, text="Update Attendance", font=("Arial", 14), width=30, bg="#ffd700", command=update_attendance_gui).pack(pady=10)
    tk.Button(window, text="Delete Attendance Record", font=("Arial", 14), width=30, bg="#ff7f7f", command=delete_attendance_gui).pack(pady=10)

    tk.Button(window, text="Back to Main Menu", font=("Arial", 14), width=30, bg="#d3d3d3", command=window.destroy).pack(pady=20)

    window.mainloop()

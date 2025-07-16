import tkinter as tk
from tkinter import messagebox
from utils.db_connection import fetch_one
from gui.gui_main import open_main_dashboard

def login_screen():
    def attempt_login():
        email = email_entry.get()
        password = password_entry.get()

        user = fetch_one("SELECT id, name, role FROM employees WHERE email = ? AND password = ?", (email, password))
        if user:
            login_window.destroy()
            open_main_dashboard(user[0], user[1], user[2])
        else:
            messagebox.showerror("Login Failed", "Invalid email or password.")

    login_window = tk.Tk()
    login_window.title("Employee Management Login")
    login_window.geometry("400x300")

    tk.Label(login_window, text="Login", font=("Arial", 20)).pack(pady=10)

    tk.Label(login_window, text="Email:").pack(pady=5)
    email_entry = tk.Entry(login_window, width=30)
    email_entry.pack()

    tk.Label(login_window, text="Password:").pack(pady=5)
    password_entry = tk.Entry(login_window, show="*", width=30)
    password_entry.pack()

    tk.Button(login_window, text="Login", width=20, command=attempt_login).pack(pady=20)

    login_window.mainloop()

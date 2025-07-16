import tkinter as tk
from tkinter import messagebox
from core.performance import add_performance, view_performance, update_performance, delete_performance
from db.performance_db import add_performance as db_add_performance, get_all_performance

def performance_gui():
    def submit():
        emp_id = entry_emp_id.get()
        rating = entry_rating.get()
        comments = entry_comments.get()

        if not emp_id or not rating or not comments:
            messagebox.showerror("Error", "All fields are required!")
            return

        try:
            db_add_performance(int(emp_id), int(rating), comments)
            messagebox.showinfo("Success", "Performance record added.")
            show_performance()
        except Exception as e:
            messagebox.showerror("Database Error", str(e))

    def show_performance():
        perf_list.delete(0, tk.END)
        try:
            performances = get_all_performance()
            for perf in performances:
                perf_list.insert(tk.END, f"{perf[0]} - EmpID: {perf[1]}, Rating: {perf[2]}, Comments: {perf[3]}")
        except Exception as e:
            messagebox.showerror("Database Error", str(e))

    win = tk.Toplevel()
    win.title("Performance Management")
    win.geometry("500x500")

    tk.Label(win, text="Employee ID").pack()
    entry_emp_id = tk.Entry(win)
    entry_emp_id.pack()

    tk.Label(win, text="Rating (1-10)").pack()
    entry_rating = tk.Entry(win)
    entry_rating.pack()

    tk.Label(win, text="Comments").pack()
    entry_comments = tk.Entry(win)
    entry_comments.pack()

    tk.Button(win, text="Submit", command=submit).pack(pady=5)

    # Performance list
    tk.Label(win, text="Performance Records").pack(pady=10)
    perf_list = tk.Listbox(win, width=80)
    perf_list.pack()

    tk.Button(win, text="Refresh", command=show_performance).pack(pady=5)

    show_performance()

def add_performance_gui():
    win = tk.Toplevel()
    win.title("Add Performance")
    win.geometry("300x300")

    tk.Label(win, text="Employee ID").pack(pady=5)
    entry_employee_id = tk.Entry(win)
    entry_employee_id.pack(pady=5)

    tk.Label(win, text="Review Date (YYYY-MM-DD)").pack(pady=5)
    entry_review_date = tk.Entry(win)
    entry_review_date.pack(pady=5)

    tk.Label(win, text="Score").pack(pady=5)
    entry_score = tk.Entry(win)
    entry_score.pack(pady=5)

    tk.Label(win, text="Comments").pack(pady=5)
    entry_comments = tk.Entry(win)
    entry_comments.pack(pady=5)

    def submit():
        employee_id = entry_employee_id.get().strip()
        review_date = entry_review_date.get().strip()
        score = entry_score.get().strip()
        comments = entry_comments.get().strip()
        if not employee_id or not review_date or not score or not comments:
            messagebox.showerror("Error", "All fields are required.")
            return
        try:
            add_performance(employee_id, review_date, score, comments)
            messagebox.showinfo("Success", "Performance added successfully.")
            win.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to add performance: {e}")

    tk.Button(win, text="Submit", command=submit).pack(pady=10)
    tk.Button(win, text="Close", command=win.destroy).pack(pady=5)

def view_performance_gui():
    win = tk.Toplevel()
    win.title("View Performance")
    win.geometry("400x300")

    performance_list = tk.Listbox(win, width=50)
    performance_list.pack(pady=10)

    try:
        performances = view_performance()
        for performance in performances:
            performance_list.insert(tk.END, f"{performance[0]} - {performance[1]} - {performance[2]} - {performance[3]}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to load performance data: {e}")

    tk.Button(win, text="Close", command=win.destroy).pack(pady=10)

def update_performance_gui():
    win = tk.Toplevel()
    win.title("Update Performance")
    win.geometry("300x300")

    tk.Label(win, text="Performance ID").pack(pady=5)
    entry_performance_id = tk.Entry(win)
    entry_performance_id.pack(pady=5)

    tk.Label(win, text="New Score").pack(pady=5)
    entry_score = tk.Entry(win)
    entry_score.pack(pady=5)

    tk.Label(win, text="New Comments").pack(pady=5)
    entry_comments = tk.Entry(win)
    entry_comments.pack(pady=5)

    def submit():
        performance_id = entry_performance_id.get().strip()
        score = entry_score.get().strip()
        comments = entry_comments.get().strip()
        if not performance_id or not score or not comments:
            messagebox.showerror("Error", "All fields are required.")
            return
        try:
            update_performance(performance_id, score, comments)
            messagebox.showinfo("Success", "Performance updated successfully.")
            win.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to update performance: {e}")

    tk.Button(win, text="Submit", command=submit).pack(pady=10)
    tk.Button(win, text="Close", command=win.destroy).pack(pady=5)

def delete_performance_gui():
    win = tk.Toplevel()
    win.title("Delete Performance")
    win.geometry("300x200")

    tk.Label(win, text="Performance ID").pack(pady=5)
    entry_performance_id = tk.Entry(win)
    entry_performance_id.pack(pady=5)

    def submit():
        performance_id = entry_performance_id.get().strip()
        if not performance_id:
            messagebox.showerror("Error", "Performance ID is required.")
            return
        try:
            delete_performance(performance_id)
            messagebox.showinfo("Success", "Performance deleted successfully.")
            win.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to delete performance: {e}")

    tk.Button(win, text="Submit", command=submit).pack(pady=10)
    tk.Button(win, text="Close", command=win.destroy).pack(pady=5)

import tkinter as tk
from tkinter import messagebox
from core.attendance_db import mark_attendance
from db.attendance_db import view_attendance, update_attendance, delete_attendance

def mark_attendance_gui():
    win = tk.Toplevel()
    win.title("Mark Attendance")
    win.geometry("300x200")

    tk.Label(win, text="Employee ID").pack(pady=5)
    entry_emp_id = tk.Entry(win)
    entry_emp_id.pack(pady=5)

    tk.Label(win, text="Date (YYYY-MM-DD)").pack(pady=5)
    entry_date = tk.Entry(win)
    entry_date.pack(pady=5)

    tk.Label(win, text="Status (Present/Absent)").pack(pady=5)
    entry_status = tk.Entry(win)
    entry_status.pack(pady=5)

    def submit():
        emp_id = entry_emp_id.get().strip()
        date = entry_date.get().strip()
        status = entry_status.get().strip()
        if not emp_id or not date or not status:
            messagebox.showerror("Error", "All fields are required.")
            return
        try:
            mark_attendance(int(emp_id), date, status)  # Pass three arguments
            messagebox.showinfo("Success", "Attendance marked successfully.")
            win.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to mark attendance: {e}")

    tk.Button(win, text="Submit", command=submit).pack(pady=10)
    tk.Button(win, text="Close", command=win.destroy).pack(pady=5)

def view_attendance_gui():
    # Create a new window for viewing attendance
    win = tk.Toplevel()
    win.title("View Attendance")
    win.geometry("600x400")

    attendance_list = tk.Listbox(win, width=80)
    attendance_list.pack(pady=10)

    try:
        records = view_attendance()  # Fetch attendance records from the database
        for record in records:
            attendance_list.insert(
                tk.END,
                f"ID: {record[0]}, EmpID: {record[1]}, Date: {record[2]}, Status: {record[3]}"
            )
    except Exception as e:
        messagebox.showerror("Error", f"Failed to load attendance: {e}")

    tk.Button(win, text="Close", command=win.destroy).pack(pady=10)

def update_attendance_gui():
    # Create a new window for updating attendance
    win = tk.Toplevel()
    win.title("Update Attendance")
    win.geometry("300x200")

    tk.Label(win, text="Attendance ID").pack(pady=5)
    entry_attendance_id = tk.Entry(win)
    entry_attendance_id.pack(pady=5)

    tk.Label(win, text="New Status (Present/Absent)").pack(pady=5)
    entry_new_status = tk.Entry(win)
    entry_new_status.pack(pady=5)

    def submit():
        attendance_id = entry_attendance_id.get().strip()
        new_status = entry_new_status.get().strip()
        if not attendance_id or not new_status:
            messagebox.showerror("Error", "Both fields are required.")
            return
        try:
            update_attendance(attendance_id, new_status)  # Call the database function
            messagebox.showinfo("Success", "Attendance updated successfully.")
            win.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to update attendance: {e}")

    tk.Button(win, text="Submit", command=submit).pack(pady=10)
    tk.Button(win, text="Close", command=win.destroy).pack(pady=5)

def delete_attendance_gui():
    # Create a new window for deleting attendance
    win = tk.Toplevel()
    win.title("Delete Attendance")
    win.geometry("300x200")

    tk.Label(win, text="Attendance ID").pack(pady=5)
    entry_attendance_id = tk.Entry(win)
    entry_attendance_id.pack(pady=5)

    def submit():
        attendance_id = entry_attendance_id.get().strip()
        if not attendance_id:
            messagebox.showerror("Error", "Attendance ID is required.")
            return
        try:
            delete_attendance(attendance_id)  # Call the database function
            messagebox.showinfo("Success", "Attendance deleted successfully.")
            win.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to delete attendance: {e}")

    tk.Button(win, text="Submit", command=submit).pack(pady=10)
    tk.Button(win, text="Close", command=win.destroy).pack(pady=5)

def attendance_gui():
    win = tk.Toplevel()
    win.title("Attendance Management")
    win.geometry("600x400")

    attendance_list = tk.Listbox(win, width=80)
    attendance_list.pack(pady=10)

    def refresh_attendance_list():
        attendance_list.delete(0, tk.END)
        try:
            records = view_attendance()
            for record in records:
                attendance_list.insert(
                    tk.END,
                    f"ID: {record[0]}, EmpID: {record[1]}, Date: {record[2]}, Status: {record[3]}"
                )
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load attendance: {e}")

    tk.Button(win, text="Mark Attendance", command=mark_attendance_gui).pack(pady=5)
    tk.Button(win, text="Update Attendance", command=update_attendance_gui).pack(pady=5)
    tk.Button(win, text="Delete Attendance", command=delete_attendance_gui).pack(pady=5)
    tk.Button(win, text="Refresh", command=refresh_attendance_list).pack(pady=5)

    refresh_attendance_list()

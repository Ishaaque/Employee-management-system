import tkinter as tk
from tkinter import messagebox
from db.leave_db import apply_leave, view_leaves, update_leave_status, delete_leave  # Import database functions

def apply_leave_gui():
    # Create a new window for applying for leave
    win = tk.Toplevel()
    win.title("Apply for Leave")
    win.geometry("300x300")

    tk.Label(win, text="Employee ID").pack(pady=5)
    entry_emp_id = tk.Entry(win)
    entry_emp_id.pack(pady=5)

    tk.Label(win, text="Start Date (YYYY-MM-DD)").pack(pady=5)
    entry_start_date = tk.Entry(win)
    entry_start_date.pack(pady=5)

    tk.Label(win, text="End Date (YYYY-MM-DD)").pack(pady=5)
    entry_end_date = tk.Entry(win)
    entry_end_date.pack(pady=5)

    tk.Label(win, text="Reason").pack(pady=5)
    entry_reason = tk.Entry(win)
    entry_reason.pack(pady=5)

    def submit():
        emp_id = entry_emp_id.get().strip()
        start_date = entry_start_date.get().strip()
        end_date = entry_end_date.get().strip()
        reason = entry_reason.get().strip()
        if not emp_id or not start_date or not end_date or not reason:
            messagebox.showerror("Error", "All fields are required.")
            return
        try:
            apply_leave(emp_id, start_date, end_date, reason)  # Call the database function to apply for leave
            messagebox.showinfo("Success", "Leave applied successfully.")
            win.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to apply for leave: {e}")

    tk.Button(win, text="Submit", command=submit).pack(pady=10)
    tk.Button(win, text="Close", command=win.destroy).pack(pady=5)

def leave_management_gui():
    win = tk.Toplevel()
    win.title("Leave Management")
    win.geometry("600x400")

    leave_list = tk.Listbox(win, width=80)
    leave_list.pack(pady=10)

    def refresh_leave_list():
        leave_list.delete(0, tk.END)
        try:
            leaves = view_leaves()  # Fetch leave data from the database
            for leave in leaves:
                leave_list.insert(
                    tk.END,
                    f"ID: {leave[0]}, EmpID: {leave[1]}, Start: {leave[2]}, End: {leave[3]}, Reason: {leave[4]}, Status: {leave[5]}"
                )
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load leaves: {e}")

    def update_leave_gui():
        update_win = tk.Toplevel()
        update_win.title("Update Leave Status")
        update_win.geometry("300x200")

        tk.Label(update_win, text="Leave ID").pack(pady=5)
        entry_leave_id = tk.Entry(update_win)
        entry_leave_id.pack(pady=5)

        tk.Label(update_win, text="New Status (Approved/Rejected)").pack(pady=5)
        entry_status = tk.Entry(update_win)
        entry_status.pack(pady=5)

        def submit():
            leave_id = entry_leave_id.get().strip()
            status = entry_status.get().strip()
            if not leave_id or not status:
                messagebox.showerror("Error", "Both fields are required.")
                return
            try:
                update_leave_status(leave_id, status)  # Update leave status in the database
                messagebox.showinfo("Success", "Leave status updated successfully.")
                update_win.destroy()
                refresh_leave_list()  # Refresh the leave list in real-time
            except Exception as e:
                messagebox.showerror("Error", f"Failed to update leave status: {e}")

        tk.Button(update_win, text="Submit", command=submit).pack(pady=10)
        tk.Button(update_win, text="Close", command=update_win.destroy).pack(pady=5)

    def delete_leave_gui():
        delete_win = tk.Toplevel()
        delete_win.title("Delete Leave")
        delete_win.geometry("300x200")

        tk.Label(delete_win, text="Leave ID").pack(pady=5)
        entry_leave_id = tk.Entry(delete_win)
        entry_leave_id.pack(pady=5)

        def submit():
            leave_id = entry_leave_id.get().strip()
            if not leave_id:
                messagebox.showerror("Error", "Leave ID is required.")
                return
            try:
                delete_leave(leave_id)  # Delete leave from the database
                messagebox.showinfo("Success", "Leave deleted successfully.")
                delete_win.destroy()
                refresh_leave_list()  # Refresh the leave list in real-time
            except Exception as e:
                messagebox.showerror("Error", f"Failed to delete leave: {e}")

        tk.Button(delete_win, text="Submit", command=submit).pack(pady=10)
        tk.Button(delete_win, text="Close", command=delete_win.destroy).pack(pady=5)

    tk.Button(win, text="Apply for Leave", command=apply_leave_gui).pack(pady=5)
    tk.Button(win, text="Update Leave Status", command=update_leave_gui).pack(pady=5)
    tk.Button(win, text="Delete Leave", command=delete_leave_gui).pack(pady=5)
    tk.Button(win, text="Refresh", command=refresh_leave_list).pack(pady=5)

    refresh_leave_list()  # Load leave data when the window is opened

def view_leaves_gui():
    # Create a new window for viewing leaves
    win = tk.Toplevel()
    win.title("View Leaves")
    win.geometry("600x400")

    leave_list = tk.Listbox(win, width=80)
    leave_list.pack(pady=10)

    try:
        leaves = view_leaves()  # Fetch leave data from the database
        for leave in leaves:
            leave_list.insert(
                tk.END,
                f"ID: {leave[0]}, EmpID: {leave[1]}, Start: {leave[2]}, End: {leave[3]}, Reason: {leave[4]}, Status: {leave[5]}"
            )
    except Exception as e:
        messagebox.showerror("Error", f"Failed to load leaves: {e}")

    tk.Button(win, text="Close", command=win.destroy).pack(pady=10)

def approve_leave_gui():
    # Create a new window for approving leave
    win = tk.Toplevel()
    win.title("Approve Leave")
    win.geometry("300x200")

    tk.Label(win, text="Leave ID").pack(pady=5)
    entry_leave_id = tk.Entry(win)
    entry_leave_id.pack(pady=5)

    def submit():
        leave_id = entry_leave_id.get().strip()
        if not leave_id:
            messagebox.showerror("Error", "Leave ID is required.")
            return
        try:
            update_leave_status(leave_id, "Approved")  # Update leave status to "Approved" in the database
            messagebox.showinfo("Success", "Leave approved successfully.")
            win.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to approve leave: {e}")

    tk.Button(win, text="Submit", command=submit).pack(pady=10)
    tk.Button(win, text="Close", command=win.destroy).pack(pady=5)

def reject_leave_gui():
    # Create a new window for rejecting leave
    win = tk.Toplevel()
    win.title("Reject Leave")
    win.geometry("300x200")

    tk.Label(win, text="Leave ID").pack(pady=5)
    entry_leave_id = tk.Entry(win)
    entry_leave_id.pack(pady=5)

    def submit():
        leave_id = entry_leave_id.get().strip()
        if not leave_id:
            messagebox.showerror("Error", "Leave ID is required.")
            return
        try:
            update_leave_status(leave_id, "Rejected")  # Update leave status to "Rejected" in the database
            messagebox.showinfo("Success", "Leave rejected successfully.")
            win.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to reject leave: {e}")

    tk.Button(win, text="Submit", command=submit).pack(pady=10)
    tk.Button(win, text="Close", command=win.destroy).pack(pady=5)

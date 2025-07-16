import tkinter as tk
from tkinter import messagebox
from core.employee import calculate_employee_salary  # Import the salary calculation function
from db.salary_db import fetch_all_salaries, update_employee_salary, delete_employee_salary  # Import the delete_employee_salary function

def salary_gui():
    win = tk.Toplevel()
    win.title("Salary Management")
    win.geometry("600x400")

    salary_list = tk.Listbox(win, width=80)
    salary_list.pack(pady=10)

    def refresh_salary_list():
        salary_list.delete(0, tk.END)
        try:
            salaries = fetch_all_salaries()  # Fetch salary data from the database
            for salary in salaries:
                salary_list.insert(
                    tk.END,
                    f"EmpID: {salary[0]}, Name: {salary[1]}, Total Salary: {salary[2]}"
                )
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load salaries: {e}")

    def calculate_salary_gui():
        calc_win = tk.Toplevel()
        calc_win.title("Calculate Salary")
        calc_win.geometry("300x200")

        tk.Label(calc_win, text="Employee ID").pack(pady=5)
        entry_emp_id = tk.Entry(calc_win)
        entry_emp_id.pack(pady=5)

        def submit():
            emp_id = entry_emp_id.get().strip()
            if not emp_id:
                messagebox.showerror("Error", "Employee ID is required.")
                return
            try:
                total_salary = calculate_employee_salary(emp_id)  # Calculate salary in real-time
                messagebox.showinfo("Success", f"Total Salary: {total_salary}")
                calc_win.destroy()
                refresh_salary_list()  # Refresh the salary list in real-time
            except Exception as e:
                messagebox.showerror("Error", f"Failed to calculate salary: {e}")

        tk.Button(calc_win, text="Submit", command=submit).pack(pady=10)
        tk.Button(calc_win, text="Close", command=calc_win.destroy).pack(pady=5)

    tk.Button(win, text="Calculate Salary", command=calculate_salary_gui).pack(pady=5)
    tk.Button(win, text="Update Salary", command=update_salary_gui).pack(pady=5)
    tk.Button(win, text="Delete Salary", command=delete_salary_gui).pack(pady=5)
    tk.Button(win, text="Refresh", command=refresh_salary_list).pack(pady=5)

    refresh_salary_list()  # Load salary data when the window is opened

def calculate_salary_gui():
    # Create a new window for calculating salary
    win = tk.Toplevel()
    win.title("Calculate Salary")
    win.geometry("300x200")

    tk.Label(win, text="Employee ID").pack(pady=5)
    entry_emp_id = tk.Entry(win)
    entry_emp_id.pack(pady=5)

    def submit():
        emp_id = entry_emp_id.get().strip()
        if not emp_id:
            messagebox.showerror("Error", "Employee ID is required.")
            return
        try:
            total_salary = calculate_employee_salary(emp_id)  # Calculate salary in real-time
            messagebox.showinfo("Success", f"Total Salary: {total_salary}")
            win.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to calculate salary: {e}")

    tk.Button(win, text="Submit", command=submit).pack(pady=10)
    tk.Button(win, text="Close", command=win.destroy).pack(pady=5)

def update_salary_gui():
    # Ensure this function is defined at the module level
    # Create a new window for updating salary
    win = tk.Toplevel()
    win.title("Update Salary")
    win.geometry("300x200")

    tk.Label(win, text="Employee ID").pack(pady=5)
    entry_emp_id = tk.Entry(win)
    entry_emp_id.pack(pady=5)

    tk.Label(win, text="New Salary").pack(pady=5)
    entry_new_salary = tk.Entry(win)
    entry_new_salary.pack(pady=5)

    def submit():
        emp_id = entry_emp_id.get().strip()
        new_salary = entry_new_salary.get().strip()
        if not emp_id or not new_salary:
            messagebox.showerror("Error", "Both fields are required.")
            return
        try:
            update_employee_salary(emp_id, float(new_salary))  # Update salary in the database
            messagebox.showinfo("Success", "Salary updated successfully.")
            win.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to update salary: {e}")

    tk.Button(win, text="Submit", command=submit).pack(pady=10)
    tk.Button(win, text="Close", command=win.destroy).pack(pady=5)

def delete_salary_gui():
    # Ensure this function is defined at the module level
    # Create a new window for deleting salary records
    win = tk.Toplevel()
    win.title("Delete Salary Record")
    win.geometry("300x200")

    tk.Label(win, text="Employee ID").pack(pady=5)
    entry_emp_id = tk.Entry(win)
    entry_emp_id.pack(pady=5)

    def submit():
        emp_id = entry_emp_id.get().strip()
        if not emp_id:
            messagebox.showerror("Error", "Employee ID is required.")
            return
        try:
            delete_employee_salary(emp_id)  # Call the database function to delete the salary record
            messagebox.showinfo("Success", "Salary record deleted successfully.")
            win.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to delete salary record: {e}")

    tk.Button(win, text="Submit", command=submit).pack(pady=10)
    tk.Button(win, text="Close", command=win.destroy).pack(pady=5)

def view_salary_gui():
    # Create a new window for viewing salaries
    win = tk.Toplevel()
    win.title("View Salaries")
    win.geometry("600x400")

    salary_list = tk.Listbox(win, width=80)
    salary_list.pack(pady=10)

    try:
        salaries = fetch_all_salaries()  # Fetch salary data from the database
        for salary in salaries:
            salary_list.insert(
                tk.END,
                f"EmpID: {salary[0]}, Name: {salary[1]}, Total Salary: {salary[2]}"
            )
    except Exception as e:
        messagebox.showerror("Error", f"Failed to load salaries: {e}")

    tk.Button(win, text="Close", command=win.destroy).pack(pady=10)

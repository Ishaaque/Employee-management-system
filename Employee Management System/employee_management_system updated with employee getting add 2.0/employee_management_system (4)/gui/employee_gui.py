import tkinter as tk
from tkinter import messagebox
from core.employee_db import add_employee, view_employees, update_employee, delete_employee

def add_employee_gui():
    def submit():
        name = entry_name.get()
        age = entry_age.get()
        gender = entry_gender.get()
        position = entry_position.get()
        salary = entry_salary.get()
        if not name or not age or not gender or not position or not salary:
            messagebox.showerror("Error", "All fields are required!")
            return
        try:
            add_employee(name, int(age), gender, position, float(salary))
            messagebox.showinfo("Success", "Employee added successfully.")
            win.destroy()
        except Exception as e:
            messagebox.showerror("Database Error", str(e))

    win = tk.Toplevel()
    win.title("Add New Employee")
    win.geometry("400x400")

    tk.Label(win, text="Name").pack(pady=5)
    entry_name = tk.Entry(win)
    entry_name.pack()

    tk.Label(win, text="Age").pack(pady=5)
    entry_age = tk.Entry(win)
    entry_age.pack()

    tk.Label(win, text="Gender").pack(pady=5)
    entry_gender = tk.Entry(win)
    entry_gender.pack()

    tk.Label(win, text="Position").pack(pady=5)
    entry_position = tk.Entry(win)
    entry_position.pack()

    tk.Label(win, text="Salary").pack(pady=5)
    entry_salary = tk.Entry(win)
    entry_salary.pack()

    tk.Button(win, text="Submit", command=submit).pack(pady=20)

def view_employees_gui():
    win = tk.Toplevel()
    win.title("All Employees")
    win.geometry("600x400")

    data = view_employees()
    if not data:
        messagebox.showinfo("No Data", "No employees found.")
        return

    text = tk.Text(win)
    text.pack(expand=True, fill="both")

    for emp in data:
        text.insert(tk.END, f"ID: {emp['id']}, Name: {emp['name']}, Age: {emp['age']}, Gender: {emp['gender']}, "
                            f"Designation: {emp.get('designation', 'N/A')}, Salary: {emp.get('salary', 'N/A')}\n")

def update_employee_gui():
    def submit_update():
        try:
            employee_id = int(entry_id.get())
            name = entry_name.get()
            age = int(entry_age.get())
            gender = entry_gender.get()
            position = entry_position.get()
            salary = float(entry_salary.get())
            update_employee(employee_id, name, age, gender, position, salary)
            messagebox.showinfo("Updated", "Employee updated successfully.")
            win.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    win = tk.Toplevel()
    win.title("Update Employee")
    win.geometry("400x400")

    tk.Label(win, text="Employee ID").pack(pady=5)
    entry_id = tk.Entry(win)
    entry_id.pack()

    tk.Label(win, text="New Name").pack(pady=5)
    entry_name = tk.Entry(win)
    entry_name.pack()

    tk.Label(win, text="New Age").pack(pady=5)
    entry_age = tk.Entry(win)
    entry_age.pack()

    tk.Label(win, text="New Gender").pack(pady=5)
    entry_gender = tk.Entry(win)
    entry_gender.pack()

    tk.Label(win, text="New Position").pack(pady=5)
    entry_position = tk.Entry(win)
    entry_position.pack()

    tk.Label(win, text="New Salary").pack(pady=5)
    entry_salary = tk.Entry(win)
    entry_salary.pack()

    tk.Button(win, text="Update", command=submit_update).pack(pady=20)

def delete_employee_gui():
    def submit_delete():
        try:
            employee_id = int(entry_id.get())
            delete_employee(employee_id)
            messagebox.showinfo("Deleted", "Employee deleted successfully.")
            win.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    win = tk.Toplevel()
    win.title("Delete Employee")
    win.geometry("300x200")

    tk.Label(win, text="Employee ID to Delete").pack(pady=10)
    entry_id = tk.Entry(win)
    entry_id.pack()

    tk.Button(win, text="Delete", command=submit_delete).pack(pady=20)

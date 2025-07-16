import tkinter as tk
from tkinter import messagebox
from core.department import add_department, view_departments, update_department, delete_department

def add_department_gui():
    win = tk.Toplevel()
    win.title("Add Department")
    win.geometry("300x250")

    tk.Label(win, text="Department Name").pack(pady=5)
    entry_name = tk.Entry(win)
    entry_name.pack(pady=5)

    tk.Label(win, text="Description").pack(pady=5)
    entry_description = tk.Entry(win)
    entry_description.pack(pady=5)

    def submit():
        name = entry_name.get().strip()
        description = entry_description.get().strip()
        if not name or not description:
            messagebox.showerror("Error", "Both fields are required.")
            return
        try:
            add_department(name, description)  # Call the function with both arguments
            messagebox.showinfo("Success", "Department added successfully.")
            win.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to add department: {e}")

    tk.Button(win, text="Submit", command=submit).pack(pady=10)
    tk.Button(win, text="Close", command=win.destroy).pack(pady=5)

def view_departments_gui():
    win = tk.Toplevel()
    win.title("View Departments")
    win.geometry("400x300")

    department_list = tk.Listbox(win, width=50)
    department_list.pack(pady=10)

    try:
        departments = view_departments()  # Assuming this function fetches department data
        for dept in departments:
            department_list.insert(tk.END, f"{dept[0]} - {dept[1]}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to load departments: {e}")

    tk.Button(win, text="Close", command=win.destroy).pack(pady=10)

def update_department_gui():
    win = tk.Toplevel()
    win.title("Update Department")
    win.geometry("300x250")

    tk.Label(win, text="Department ID").pack(pady=5)
    entry_id = tk.Entry(win)
    entry_id.pack(pady=5)

    tk.Label(win, text="New Department Name").pack(pady=5)
    entry_name = tk.Entry(win)
    entry_name.pack(pady=5)

    tk.Label(win, text="New Description").pack(pady=5)
    entry_description = tk.Entry(win)
    entry_description.pack(pady=5)

    def submit():
        dept_id = entry_id.get().strip()
        name = entry_name.get().strip()
        description = entry_description.get().strip()
        if not dept_id or not name or not description:
            messagebox.showerror("Error", "All fields are required.")
            return
        try:
            update_department(dept_id, name, description)  # Call the function with all arguments
            messagebox.showinfo("Success", "Department updated successfully.")
            win.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to update department: {e}")

    tk.Button(win, text="Submit", command=submit).pack(pady=10)
    tk.Button(win, text="Close", command=win.destroy).pack(pady=5)

def delete_department_gui():
    win = tk.Toplevel()
    win.title("Delete Department")
    win.geometry("300x200")

    tk.Label(win, text="Department ID").pack(pady=5)
    entry_id = tk.Entry(win)
    entry_id.pack(pady=5)

    def submit():
        dept_id = entry_id.get().strip()
        if not dept_id:
            messagebox.showerror("Error", "Department ID is required.")
            return
        try:
            delete_department(dept_id)  # Assuming this function deletes a department from the database
            messagebox.showinfo("Success", "Department deleted successfully.")
            win.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to delete department: {e}")

    tk.Button(win, text="Submit", command=submit).pack(pady=10)
    tk.Button(win, text="Close", command=win.destroy).pack(pady=5)

def department_gui():
    def refresh_department_list():
        department_list.delete(0, tk.END)
        departments = view_departments()
        for dept in departments:
            department_list.insert(tk.END, f"{dept[0]} - {dept[1]}")

    def add():
        name = entry_name.get().strip()
        if not name:
            messagebox.showerror("Error", "Department name is required.")
            return
        try:
            add_department(name)
            messagebox.showinfo("Success", "Department added successfully.")
            entry_name.delete(0, tk.END)
            refresh_department_list()
        except Exception as e:
            messagebox.showerror("Database Error", str(e))

    def update():
        selected = department_list.curselection()
        if not selected:
            messagebox.showerror("Error", "Select a department to update.")
            return
        index = selected[0]
        dept_id = int(department_list.get(index).split(" - ")[0])
        name = entry_name.get().strip()
        if not name:
            messagebox.showerror("Error", "Department name is required.")
            return
        try:
            update_department(dept_id, name)
            messagebox.showinfo("Success", "Department updated successfully.")
            refresh_department_list()
        except Exception as e:
            messagebox.showerror("Database Error", str(e))

    def delete():
        selected = department_list.curselection()
        if not selected:
            messagebox.showerror("Error", "Select a department to delete.")
            return
        index = selected[0]
        dept_id = int(department_list.get(index).split(" - ")[0])
        try:
            delete_department(dept_id)
            messagebox.showinfo("Success", "Department deleted successfully.")
            refresh_department_list()
        except Exception as e:
            messagebox.showerror("Database Error", str(e))

    win = tk.Toplevel()
    win.title("Manage Departments")
    win.geometry("400x400")

    tk.Label(win, text="Department Name").pack(pady=5)
    entry_name = tk.Entry(win)
    entry_name.pack(pady=5)

    department_list = tk.Listbox(win)  # Initialize department_list
    department_list.pack(pady=5)

    tk.Button(win, text="Add", command=add).pack(pady=5)
    tk.Button(win, text="Update", command=update).pack(pady=5)
    tk.Button(win, text="Delete", command=delete).pack(pady=5)

    refresh_department_list()

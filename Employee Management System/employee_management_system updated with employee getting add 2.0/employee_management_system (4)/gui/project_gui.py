import tkinter as tk
from tkinter import messagebox
from db.project_db import add_project, assign_employee_to_project, view_all_projects, update_project, remove_project
from core.project import assign_project, view_projects

def project_gui():
    def submit_project():
        name = entry_name.get()
        description = entry_description.get()
        deadline = entry_deadline.get()

        if not name or not description or not deadline:
            messagebox.showerror("Error", "All fields are required!")
            return

        try:
            add_project(name, description, deadline)  # Add project to the database
            messagebox.showinfo("Success", "Project added.")
            show_projects()  # Refresh the project list
        except Exception as e:
            messagebox.showerror("Database Error", str(e))

    def assign_employee():
        proj_id = entry_proj_id.get()
        emp_id = entry_emp_id.get()

        if not proj_id or not emp_id:
            messagebox.showerror("Error", "Both fields are required!")
            return

        try:
            assign_employee_to_project(int(proj_id), int(emp_id))  # Assign employee to project
            messagebox.showinfo("Success", "Employee assigned to project.")
        except Exception as e:
            messagebox.showerror("Database Error", str(e))

    def show_projects():
        project_list.delete(0, tk.END)
        try:
            projects = view_all_projects()  # Fetch projects from the database
            for proj in projects:
                project_list.insert(tk.END, f"{proj[0]} - {proj[1]} | Deadline: {proj[3]}")
        except Exception as e:
            messagebox.showerror("Database Error", str(e))

    win = tk.Toplevel()
    win.title("Project Management")
    win.geometry("600x600")

    tk.Label(win, text="Project Name").pack()
    entry_name = tk.Entry(win)
    entry_name.pack()

    tk.Label(win, text="Description").pack()
    entry_description = tk.Entry(win)
    entry_description.pack()

    tk.Label(win, text="Deadline (YYYY-MM-DD)").pack()
    entry_deadline = tk.Entry(win)
    entry_deadline.pack()

    tk.Button(win, text="Add Project", command=submit_project).pack(pady=5)

    tk.Label(win, text="Assign Employee to Project").pack(pady=10)
    tk.Label(win, text="Project ID").pack()
    entry_proj_id = tk.Entry(win)
    entry_proj_id.pack()

    tk.Label(win, text="Employee ID").pack()
    entry_emp_id = tk.Entry(win)
    entry_emp_id.pack()

    tk.Button(win, text="Assign", command=assign_employee).pack(pady=5)

    tk.Label(win, text="All Projects").pack(pady=10)
    project_list = tk.Listbox(win, width=80)
    project_list.pack()

    tk.Button(win, text="Refresh", command=show_projects).pack(pady=5)

    show_projects()  # Load projects when the window is opened

def assign_project_gui():
    win = tk.Toplevel()
    win.title("Assign Project")
    win.geometry("300x200")

    tk.Label(win, text="Project ID").pack(pady=5)
    entry_project_id = tk.Entry(win)
    entry_project_id.pack(pady=5)

    tk.Label(win, text="Employee ID").pack(pady=5)
    entry_employee_id = tk.Entry(win)
    entry_employee_id.pack(pady=5)

    def submit():
        project_id = entry_project_id.get().strip()
        employee_id = entry_employee_id.get().strip()
        if not project_id or not employee_id:
            messagebox.showerror("Error", "Both fields are required.")
            return
        try:
            assign_project(project_id, employee_id)
            messagebox.showinfo("Success", "Project assigned successfully.")
            win.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to assign project: {e}")

    tk.Button(win, text="Submit", command=submit).pack(pady=10)
    tk.Button(win, text="Close", command=win.destroy).pack(pady=5)

def view_projects_gui():
    win = tk.Toplevel()
    win.title("View Projects")
    win.geometry("400x300")

    project_list = tk.Listbox(win, width=50)
    project_list.pack(pady=10)

    try:
        projects = view_projects()
        for project in projects:
            project_list.insert(tk.END, f"{project[0]} - {project[1]} - {project[2]}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to load projects: {e}")

    tk.Button(win, text="Close", command=win.destroy).pack(pady=10)

def update_project_gui():
    win = tk.Toplevel()
    win.title("Update Project")
    win.geometry("300x300")

    tk.Label(win, text="Project ID").pack(pady=5)
    entry_project_id = tk.Entry(win)
    entry_project_id.pack(pady=5)

    tk.Label(win, text="New Description").pack(pady=5)
    entry_description = tk.Entry(win)
    entry_description.pack(pady=5)

    tk.Label(win, text="New Deadline (YYYY-MM-DD)").pack(pady=5)
    entry_deadline = tk.Entry(win)
    entry_deadline.pack(pady=5)

    def submit():
        project_id = entry_project_id.get().strip()
        description = entry_description.get().strip()
        deadline = entry_deadline.get().strip()
        if not project_id or not description or not deadline:
            messagebox.showerror("Error", "All fields are required.")
            return
        try:
            update_project(project_id, description, deadline)  # Update project in the database
            messagebox.showinfo("Success", "Project updated successfully.")
            win.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to update project: {e}")

    tk.Button(win, text="Submit", command=submit).pack(pady=10)
    tk.Button(win, text="Close", command=win.destroy).pack(pady=5)

def remove_project_gui():
    win = tk.Toplevel()
    win.title("Remove Project")
    win.geometry("300x200")

    tk.Label(win, text="Project ID").pack(pady=5)
    entry_project_id = tk.Entry(win)
    entry_project_id.pack(pady=5)

    def submit():
        project_id = entry_project_id.get().strip()
        if not project_id:
            messagebox.showerror("Error", "Project ID is required.")
            return
        try:
            remove_project(project_id)  # Remove project from the database
            messagebox.showinfo("Success", "Project removed successfully.")
            win.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to remove project: {e}")

    tk.Button(win, text="Submit", command=submit).pack(pady=10)
    tk.Button(win, text="Close", command=win.destroy).pack(pady=5)

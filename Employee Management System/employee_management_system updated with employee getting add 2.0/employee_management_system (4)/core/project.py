from utils.db_connection import execute_query, fetch_all, fetch_one

def add_project(name, description, start_date, end_date):
    query = """
    INSERT INTO projects (name, description, start_date, end_date)
    VALUES (?, ?, ?, ?)
    """
    execute_query(query, (name, description, start_date, end_date))

def get_all_projects():
    query = "SELECT * FROM projects"
    return fetch_all(query)

def update_project(project_id, description, start_date, end_date):
    """
    Update the details of a project in the database.
    """
    query = """
    UPDATE projects
    SET description = ?, start_date = ?, end_date = ?
    WHERE id = ?
    """
    execute_query(query, (description, start_date, end_date, project_id))

def delete_project(project_id):
    query = "DELETE FROM projects WHERE id = ?"
    execute_query(query, (project_id,))

def assign_project(project_id, employee_id):
    # Placeholder implementation for assigning a project
    print(f"Project ID {project_id} assigned to Employee ID {employee_id}.")
    # Add database logic here, e.g., inserting the assignment into a table
    # Example:
    # conn = get_db_connection()
    # cursor = conn.cursor()
    # cursor.execute("INSERT INTO project_assignments (project_id, employee_id) VALUES (?, ?)", (project_id, employee_id))
    # conn.commit()
    # conn.close()

def view_projects():
    # Placeholder implementation for viewing projects
    print("Fetching all projects...")
    # Add database logic here, e.g., fetching projects from a table
    # Example:
    # conn = get_db_connection()
    # cursor = conn.cursor()
    # cursor.execute("SELECT id, name, start_date, end_date FROM projects")
    # projects = cursor.fetchall()
    # conn.close()
    # return projects
    return [
        (1, "Project Alpha", "2023-01-01", "2023-12-31"),
        (2, "Project Beta", "2023-02-01", "2023-11-30"),
    ]

def remove_project(project_id):
    # Placeholder implementation for removing a project
    print(f"Project ID {project_id} removed.")
    # Add database logic here, e.g., deleting the project from a table
    # Example:
    # conn = get_db_connection()
    # cursor = conn.cursor()
    # cursor.execute("DELETE FROM projects WHERE id = ?", (project_id,))
    # conn.commit()
    # conn.close()

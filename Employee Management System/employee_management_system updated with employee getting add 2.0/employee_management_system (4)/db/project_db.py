from utils.db_connection import execute_query, fetch_all

def add_project(name, description, deadline):
    """
    Add a new project to the database.
    """
    query = """
    INSERT INTO projects (name, description, deadline)
    VALUES (?, ?, ?)
    """
    execute_query(query, (name, description, deadline))

def assign_employee_to_project(project_id, employee_id):
    """
    Assign an employee to a project in the database.
    """
    query = """
    INSERT INTO project_assignments (project_id, employee_id)
    VALUES (?, ?)
    """
    execute_query(query, (project_id, employee_id))

def view_all_projects():
    """
    Fetch all projects from the database.
    """
    query = """
    SELECT id, name, description, deadline
    FROM projects
    """
    return fetch_all(query)

def update_project(project_id, description, deadline):
    """
    Update a project's details in the database.
    """
    query = """
    UPDATE projects
    SET description = ?, deadline = ?
    WHERE id = ?
    """
    execute_query(query, (description, deadline, project_id))

def remove_project(project_id):
    """
    Remove a project from the database.
    """
    query = "DELETE FROM projects WHERE id = ?"
    execute_query(query, (project_id,))

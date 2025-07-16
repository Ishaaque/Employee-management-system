import sqlite3
from utils.db_connection import get_db_connection, execute_query

def add_department(name, description):
    query = "INSERT INTO departments (name, description) VALUES (?, ?)"
    execute_query(query, (name, description))

def view_departments():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM departments")
        departments = cursor.fetchall()
        return departments
    except sqlite3.Error as e:
        print("Error viewing departments:", e)
        return []
    finally:
        conn.close()

def update_department(dept_id, name, description):
    query = """
    UPDATE departments
    SET name = ?, description = ?
    WHERE id = ?
    """
    execute_query(query, (name, description, dept_id))

def delete_department(department_id):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM departments WHERE id = ?", (department_id,))
        conn.commit()
        print("Department deleted successfully.")
    except sqlite3.Error as e:
        print("Error deleting department:", e)
    finally:
        conn.close()

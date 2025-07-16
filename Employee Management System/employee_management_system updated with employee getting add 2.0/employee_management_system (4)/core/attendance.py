from utils.db_connection import execute_query, fetch_all, fetch_one

def mark_attendance(employee_id, date, status):
    query = """
    INSERT INTO attendance (employee_id, date, status)
    VALUES (?, ?, ?)
    """
    execute_query(query, (employee_id, date, status))

def get_attendance_by_employee(employee_id):
    query = "SELECT * FROM attendance WHERE employee_id = ?"
    return fetch_all(query, (employee_id,))

def get_all_attendance():
    query = "SELECT * FROM attendance"
    return fetch_all(query)

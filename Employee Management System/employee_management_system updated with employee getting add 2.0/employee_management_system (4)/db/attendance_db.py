from utils.db_connection import execute_query, fetch_all  # Import required database utility functions

def mark_attendance(employee_id):
    query = "INSERT INTO attendance (employee_id, date, status) VALUES (?, DATE('now'), 'Present')"
    execute_query(query, (employee_id,))

def view_attendance():
    query = "SELECT id, employee_id, date, status FROM attendance"
    return fetch_all(query)

def update_attendance(attendance_id, status):
    query = "UPDATE attendance SET status = ? WHERE id = ?"
    execute_query(query, (status, attendance_id))

def delete_attendance(attendance_id):
    query = "DELETE FROM attendance WHERE id = ?"
    execute_query(query, (attendance_id,))

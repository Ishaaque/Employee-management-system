from utils.db_connection import execute_query, fetch_all

def apply_leave(emp_id, start_date, end_date, reason):
    query = """
    INSERT INTO leaves (employee_id, start_date, end_date, reason, status)
    VALUES (?, ?, ?, ?, 'Pending')
    """
    execute_query(query, (emp_id, start_date, end_date, reason))

def view_leaves():
    query = "SELECT id, employee_id, start_date, end_date, reason, status FROM leaves"
    return fetch_all(query)

def update_leave_status(leave_id, status):
    query = "UPDATE leaves SET status = ? WHERE id = ?"
    execute_query(query, (status, leave_id))

def delete_leave(leave_id):
    query = "DELETE FROM leaves WHERE id = ?"
    execute_query(query, (leave_id,))

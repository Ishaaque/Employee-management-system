from utils.db_connection import execute_query, fetch_all, fetch_one

def apply_leave(emp_id, start_date, end_date, reason):
    # Insert a leave request into the database
    query = """
    INSERT INTO leaves (employee_id, start_date, end_date, reason, status)
    VALUES (?, ?, ?, ?, 'Pending')
    """
    execute_query(query, (emp_id, start_date, end_date, reason))

def get_all_leave_requests():
    query = "SELECT * FROM leave_requests"
    return fetch_all(query)

def update_leave_status(leave_id, status):
    query = "UPDATE leave_requests SET status = ? WHERE id = ?"
    execute_query(query, (status, leave_id))

def get_leave_requests_by_employee(employee_id):
    query = "SELECT * FROM leave_requests WHERE employee_id = ?"
    return fetch_all(query, (employee_id,))

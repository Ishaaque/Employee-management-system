from utils.db_connection import fetch_all, execute_query

def fetch_all_salaries():
    """
    Fetch all employee salaries from the database.
    """
    query = """
    SELECT e.id AS employee_id, e.name AS employee_name, 
           (e.salary + (a.hours_worked * 100) - (a.hours_lately * 50)) AS total_salary
    FROM employees e
    LEFT JOIN attendance a ON e.id = a.employee_id
    """
    return fetch_all(query)

def calculate_salary(employee_id, hours_worked, hourly_rate):
    # Placeholder implementation for calculating salary
    return hours_worked * hourly_rate

def view_all_salaries():
    # Placeholder implementation for viewing all salaries
    return [
        {"employee_id": 1, "name": "John Doe", "salary": 5000},
        {"employee_id": 2, "name": "Jane Smith", "salary": 6000},
    ]

def update_salary(employee_id, new_salary):
    """
    Update the salary of an employee in the database.
    """
    query = "UPDATE employees SET salary = ? WHERE id = ?"
    execute_query(query, (new_salary, employee_id))

def update_employee_salary(emp_id, new_salary):
    """
    Update the salary of an employee in the database.
    """
    query = "UPDATE employees SET salary = ? WHERE id = ?"
    execute_query(query, (new_salary, emp_id))

def delete_salary(employee_id):
    # Placeholder implementation for deleting salary
    print(f"Salary record for Employee ID {employee_id} deleted.")
    # Add database logic here, e.g., deleting salary from a table
    # Example:
    # conn = get_db_connection()
    # cursor = conn.cursor()
    # cursor.execute("DELETE FROM salaries WHERE employee_id = ?", (employee_id,))
    # conn.commit()
    # conn.close()

def delete_employee_salary(emp_id):
    """
    Delete the salary record of an employee from the database.
    """
    query = "DELETE FROM employees WHERE id = ?"
    execute_query(query, (emp_id,))

from utils.db_connection import execute_query, fetch_all, fetch_one

def add_employee(id,name, age,designation, salary):
    """
    Add a new employee to the database.
    """
    query = """
    INSERT INTO employees (id,name,email,designation,salary)
    VALUES (?, ?, ?, ?, ?)
    """
    execute_query(query, (id,name, age, designation,salary))

def get_all_employees():
    query = "SELECT * FROM employees"
    return fetch_all(query)

def get_employee_by_id(emp_id):
    query = "SELECT * FROM employees WHERE id = ?"
    return fetch_one(query, (emp_id,))

def update_employee(emp_id, data):
    query = """
    UPDATE employees
    SET name = ?, email = ?, phone = ?, department_id = ?, designation = ?, hire_date = ?, salary = ?
    WHERE id = ?
    """
    execute_query(query, (*data, emp_id))

def delete_employee(emp_id):
    query = "DELETE FROM employees WHERE id = ?"
    execute_query(query, (emp_id,))

def calculate_employee_salary(employee_id):
    """
    Calculate the salary of an employee based on their base salary, hours worked, and hours lately.
    """
    query = """
    SELECT salary, hours_worked, hours_lately
    FROM employees
    WHERE id = ?
    """
    result = fetch_one(query, (employee_id,))
    if result:
        base_salary, hours_worked, hours_lately = result
        penalty_per_hour = 50  # Deduction for each late hour
        hourly_rate = 100  # Compensation for each worked hour
        total_salary = base_salary + (hours_worked * hourly_rate) - (hours_lately * penalty_per_hour)
        return max(total_salary, 0)  # Ensure salary is not negative
    else:
        raise ValueError(f"Employee with ID {employee_id} not found.")



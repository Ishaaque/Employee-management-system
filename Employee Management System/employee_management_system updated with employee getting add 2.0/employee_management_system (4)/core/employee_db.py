# core/employee_db.py

import json

# Temporary in-memory storage
employees = []
next_employee_id = 1  # Initialize auto-incrementing ID
DATA_FILE = "employees_data.json"

def load_employees_from_file():
    global employees, next_employee_id
    try:
        with open(DATA_FILE, "r") as file:
            employees_data = json.load(file)
            employees.extend(employees_data)
            if employees:
                next_employee_id = max(emp['id'] for emp in employees) + 1
    except FileNotFoundError:
        print("No existing data file found. Starting fresh.")
    except Exception as e:
        print("Error loading employee data:", str(e))

def save_employees_to_file():
    with open(DATA_FILE, "w") as file:
        json.dump(employees, file)
    print("Employee data saved to file.")

def add_employee(name, age, gender, designation, salary):
    global next_employee_id
    data = {
        'id': next_employee_id,
        'name': name,
        'age': age,
        'gender': gender,
        'designation': designation,
        'salary': salary
    }
    employees.append(data)
    next_employee_id += 1  # Increment the ID for the next employee
    save_employees_to_file()
    print("Employee added:", data)

def view_employees():
    return employees

def update_employee(emp_id, new_name, new_age, new_gender, new_position, new_salary):
    updated_data = {
        'name': new_name,
        'age': new_age,
        'gender': new_gender,
        'designation': new_position,
        'salary': new_salary
    }
    for emp in employees:
        if emp['id'] == emp_id:
            emp.update(updated_data)
            save_employees_to_file()
            print("Employee updated:", emp)
            return
    print("Employee not found.")

def delete_employee(emp_id):
    global employees
    employees = [emp for emp in employees if emp['id'] != emp_id]
    save_employees_to_file()
    print("Employee deleted with ID:", emp_id)

# Load employees when the module is imported
load_employees_from_file()

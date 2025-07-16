from utils.db_connection import fetch_one, fetch_all

def calculate_salary(employee_id):
    base_query = "SELECT salary FROM employees WHERE id = ?"
    result = fetch_one(base_query, (employee_id,))
    if result is None:
        return 0
    base_salary = result[0]

    attendance_query = "SELECT COUNT(*) FROM attendance WHERE employee_id = ? AND status = 'Absent'"
    absent_days = fetch_one(attendance_query, (employee_id,))[0]

    daily_rate = base_salary / 30
    deduction = absent_days * daily_rate
    final_salary = round(base_salary - deduction, 2)
    return final_salary

def get_salary_report():
    employees = fetch_all("SELECT id, name FROM employees")
    report = []
    for emp in employees:
        salary = calculate_salary(emp[0])
        report.append((emp[0], emp[1], salary))
    return report

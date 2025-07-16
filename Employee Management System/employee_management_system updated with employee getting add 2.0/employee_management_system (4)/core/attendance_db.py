from utils.db_connection import get_db_connection  # Ensure correct import

def mark_attendance(employee_id, date, status):
    print(f"mark_attendance called with: employee_id={employee_id}, date={date}, status={status}")  # Debugging
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO attendance (employee_id, date, status)
        VALUES (?, ?, ?)
    """, (employee_id, date, status))
    conn.commit()
    conn.close()
    print(f"Attendance marked for Employee ID {employee_id} on {date} with status {status}")
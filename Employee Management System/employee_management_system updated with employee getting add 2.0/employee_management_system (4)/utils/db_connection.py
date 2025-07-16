import sqlite3

def get_db_connection():  # Renamed from get_connection to get_db_connection
    return sqlite3.connect("employee_management.db")

def execute_query(query, params=()):
    conn = get_db_connection()  # Updated function call
    cursor = conn.cursor()
    cursor.execute(query, params)
    conn.commit()
    conn.close()

def fetch_all(query, params=()):
    conn = get_db_connection()  # Updated function call
    cursor = conn.cursor()
    cursor.execute(query, params)
    rows = cursor.fetchall()
    conn.close()
    return rows

def fetch_one(query, params=()):
    """
    Execute a SELECT query and fetch a single record.
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(query, params)
    result = cursor.fetchone()
    conn.close()
    return result

def initialize_database():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Create or update the employees table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            designation TEXT,
            salary REAL
        )
    """)
    
    # Check if the phone column exists, and add it if necessary
    cursor.execute("PRAGMA table_info(employees)")
    columns = [column[1] for column in cursor.fetchall()]
    if "phone" not in columns:
        cursor.execute("ALTER TABLE employees ADD COLUMN phone TEXT")
    # Add email column if missing
    if "email" not in columns:
        cursor.execute("ALTER TABLE employees ADD COLUMN email TEXT")
    # Add password column if missing
    if "password" not in columns:
        cursor.execute("ALTER TABLE employees ADD COLUMN password TEXT")
    # Add role column if missing
    if "role" not in columns:
        cursor.execute("ALTER TABLE employees ADD COLUMN role TEXT")
    # Check if the department_id column exists, and add it if necessary
    if "department_id" not in columns:
        cursor.execute("ALTER TABLE employees ADD COLUMN department_id INTEGER")
    
    # Check if the designation column exists, and add it if necessary
    if "designation" not in columns:
        cursor.execute("ALTER TABLE employees ADD COLUMN designation TEXT")
    
    # Check if the salary column exists, and add it if necessary
    if "salary" not in columns:
        cursor.execute("ALTER TABLE employees ADD COLUMN salary REAL")
    
    # Check if the hire_date column exists, and add it if necessary
    if "hire_date" not in columns:
        print("Adding hire_date column to employees table...")
        cursor.execute("ALTER TABLE employees ADD COLUMN hire_date TEXT")
    
    # Create or update the attendance table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS attendance (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            employee_id INTEGER NOT NULL,
            date TEXT NOT NULL,
            status TEXT NOT NULL,
            hours_worked INTEGER DEFAULT 0,  -- Add hours_worked column
            hours_lately INTEGER DEFAULT 0,  -- Add hours_lately column
            FOREIGN KEY (employee_id) REFERENCES employees (id)
        )
    """)
    
    # Check if the hours_worked and hours_lately columns exist, and add them if necessary
    cursor.execute("PRAGMA table_info(attendance)")
    columns = [column[1] for column in cursor.fetchall()]
    if "hours_worked" not in columns:
        print("Adding hours_worked column to attendance table...")
        cursor.execute("ALTER TABLE attendance ADD COLUMN hours_worked INTEGER DEFAULT 0")
    if "hours_lately" not in columns:
        print("Adding hours_lately column to attendance table...")
        cursor.execute("ALTER TABLE attendance ADD COLUMN hours_lately INTEGER DEFAULT 0")
    
    # Create or update the departments table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS departments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE,
            description TEXT NOT NULL
        )
    """)
    
    # Check if the description column exists, and add it if necessary
    cursor.execute("PRAGMA table_info(departments)")
    columns = [column[1] for column in cursor.fetchall()]
    if "description" not in columns:
        cursor.execute("ALTER TABLE departments ADD COLUMN description TEXT")
    
    # Create or update the leaves table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS leaves (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            employee_id INTEGER NOT NULL,
            start_date TEXT NOT NULL,
            end_date TEXT NOT NULL,
            reason TEXT NOT NULL,
            status TEXT NOT NULL,
            FOREIGN KEY (employee_id) REFERENCES employees (id)
        )
    """)
    
    # Create or update the projects table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS projects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT NOT NULL,
            deadline TEXT NOT NULL
        )
    """)

    # Create or update the project_assignments table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS project_assignments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            project_id INTEGER NOT NULL,
            employee_id INTEGER NOT NULL,
            FOREIGN KEY (project_id) REFERENCES projects (id),
            FOREIGN KEY (employee_id) REFERENCES employees (id)
        )
    """)
    
    # Create or update the performance_reviews table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS performance_reviews (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            employee_id INTEGER NOT NULL,
            review_date TEXT NOT NULL,
            comments TEXT NOT NULL,
            rating INTEGER NOT NULL,
            FOREIGN KEY (employee_id) REFERENCES employees (id)
        )
    """)
    
    # Insert a default user if the employees table is empty
    cursor.execute("SELECT COUNT(*) FROM employees")
    if cursor.fetchone()[0] == 0:
        cursor.execute("""
            INSERT INTO employees (name, age, email, phone, department_id, designation, hire_date, salary, password, role)
            VALUES ('Admin User', 30, 'admin@example.com', '1234567890', 1, 'Admin', '2023-01-01', 100000, 'admin123', 'admin')
        """)
    
    conn.commit()
    conn.close()

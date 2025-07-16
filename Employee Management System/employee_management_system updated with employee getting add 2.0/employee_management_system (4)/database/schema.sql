-- Employee Table
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    phone TEXT,
    department_id INTEGER,
    designation TEXT,
    hire_date TEXT,
    salary REAL,
    password TEXT NOT NULL,
    role TEXT DEFAULT 'employee',
    FOREIGN KEY (department_id) REFERENCES departments(id)
);

-- Department Table
CREATE TABLE IF NOT EXISTS departments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    location TEXT
);

-- Attendance Table
CREATE TABLE IF NOT EXISTS attendance (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    employee_id INTEGER,
    date TEXT,
    status TEXT CHECK(status IN ('Present', 'Absent', 'Leave')),
    FOREIGN KEY (employee_id) REFERENCES employees(id)
);

-- Leave Table
CREATE TABLE IF NOT EXISTS leave_requests (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    employee_id INTEGER,
    start_date TEXT,
    end_date TEXT,
    reason TEXT,
    status TEXT CHECK(status IN ('Pending', 'Approved', 'Rejected')) DEFAULT 'Pending',
    FOREIGN KEY (employee_id) REFERENCES employees(id)
);

-- Projects Table
CREATE TABLE IF NOT EXISTS projects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    description TEXT,
    start_date TEXT,
    end_date TEXT
);

-- Performance Table
CREATE TABLE IF NOT EXISTS performance (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    employee_id INTEGER,
    review_date TEXT,
    score INTEGER CHECK(score BETWEEN 1 AND 10),
    comments TEXT,
    FOREIGN KEY (employee_id) REFERENCES employees(id)
);

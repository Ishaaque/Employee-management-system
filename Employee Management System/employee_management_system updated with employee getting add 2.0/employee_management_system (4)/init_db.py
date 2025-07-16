import sqlite3

def initialize_db():
    with open("database/schema.sql", "r") as schema_file:
        schema = schema_file.read()

    conn = sqlite3.connect("employee_management.db")
    cursor = conn.cursor()
    cursor.executescript(schema)
    conn.commit()
    conn.close()
    print("Database initialized successfully.")

if __name__ == "__main__":
    initialize_db()

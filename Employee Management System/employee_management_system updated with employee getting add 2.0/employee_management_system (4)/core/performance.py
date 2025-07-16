from utils.db_connection import execute_query, fetch_all, fetch_one

def add_review(employee_id, review_date, score, comments):
    query = """
    INSERT INTO performance (employee_id, review_date, score, comments)
    VALUES (?, ?, ?, ?)
    """
    execute_query(query, (employee_id, review_date, score, comments))

def get_reviews_by_employee(employee_id):
    query = "SELECT * FROM performance WHERE employee_id = ?"
    return fetch_all(query, (employee_id,))

def get_all_reviews():
    query = "SELECT * FROM performance"
    return fetch_all(query)

def add_performance(employee_id, review_date, score, comments):
    # Placeholder implementation for adding performance data
    print(f"Performance added for Employee ID {employee_id} on {review_date} with score {score}.")
    # Add database logic here, e.g., inserting performance data into a table
    # Example:
    # conn = get_db_connection()
    # cursor = conn.cursor()
    # cursor.execute(
    #     "INSERT INTO performance (employee_id, review_date, score, comments) VALUES (?, ?, ?, ?)",
    #     (employee_id, review_date, score, comments)
    # )
    # conn.commit()
    # conn.close()

def view_performance():
    # Placeholder implementation for viewing performance data
    print("Fetching all performance records...")
    # Add database logic here, e.g., fetching performance data from a table
    # Example:
    # conn = get_db_connection()
    # cursor = conn.cursor()
    # cursor.execute("SELECT id, employee_id, review_date, score, comments FROM performance")
    # performance_records = cursor.fetchall()
    # conn.close()
    # return performance_records
    return [
        (1, 101, "2023-01-15", 85, "Excellent work"),
        (2, 102, "2023-02-20", 78, "Good performance"),
    ]

def update_performance(performance_id, score, comments):
    # Placeholder implementation for updating performance data
    print(f"Performance ID {performance_id} updated with score {score} and comments: {comments}")
    # Add database logic here, e.g., updating performance data in a table
    # Example:
    # conn = get_db_connection()
    # cursor = conn.cursor()
    # cursor.execute(
    #     "UPDATE performance SET score = ?, comments = ? WHERE id = ?",
    #     (score, comments, performance_id)
    # )
    # conn.commit()
    # conn.close()

def delete_performance(performance_id):
    # Placeholder implementation for deleting performance data
    print(f"Performance record with ID {performance_id} deleted.")
    # Add database logic here, e.g., deleting performance data from a table
    # Example:
    # conn = get_db_connection()
    # cursor = conn.cursor()
    # cursor.execute("DELETE FROM performance WHERE id = ?", (performance_id,))
    # conn.commit()
    # conn.close()

from utils.db_connection import execute_query, fetch_all, fetch_one

def add_performance_review(employee_id, review_date, comments, rating):
    """
    Add a new performance review to the database.
    """
    query = """
    INSERT INTO performance_reviews (employee_id, review_date, comments, rating)
    VALUES (?, ?, ?, ?)
    """
    execute_query(query, (employee_id, review_date, comments, rating))

def view_performance_reviews():
    """
    Fetch all performance reviews from the database.
    """
    query = """
    SELECT pr.id, e.name, pr.review_date, pr.comments, pr.rating
    FROM performance_reviews pr
    JOIN employees e ON pr.employee_id = e.id
    """
    return fetch_all(query)

def update_performance_review(review_id, comments, rating):
    """
    Update an existing performance review in the database.
    """
    query = """
    UPDATE performance_reviews
    SET comments = ?, rating = ?
    WHERE id = ?
    """
    execute_query(query, (comments, rating, review_id))

def delete_performance_review(review_id):
    """
    Delete a performance review from the database.
    """
    query = "DELETE FROM performance_reviews WHERE id = ?"
    execute_query(query, (review_id,))

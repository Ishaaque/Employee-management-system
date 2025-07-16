import tkinter as tk
from tkinter import messagebox
from db.performance_review_db import add_performance_review, view_performance_reviews, update_performance_review, delete_performance_review

def performance_review_gui():
    def submit_review():
        emp_id = entry_emp_id.get()
        review_date = entry_review_date.get()
        comments = entry_comments.get()
        rating = entry_rating.get()

        if not emp_id or not review_date or not comments or not rating:
            messagebox.showerror("Error", "All fields are required!")
            return

        try:
            add_performance_review(emp_id, review_date, comments, int(rating))  # Add review to the database
            messagebox.showinfo("Success", "Performance review added.")
            refresh_reviews()  # Refresh the review list
        except Exception as e:
            messagebox.showerror("Database Error", str(e))

    def refresh_reviews():
        review_list.delete(0, tk.END)
        try:
            reviews = view_performance_reviews()  # Fetch reviews from the database
            for review in reviews:
                review_list.insert(tk.END, f"{review[0]} - {review[1]} | {review[2]} | {review[3]} | Rating: {review[4]}")
        except Exception as e:
            messagebox.showerror("Database Error", str(e))

    def update_review():
        review_id = entry_review_id.get()
        comments = entry_update_comments.get()
        rating = entry_update_rating.get()

        if not review_id or not comments or not rating:
            messagebox.showerror("Error", "All fields are required!")
            return

        try:
            update_performance_review(review_id, comments, int(rating))  # Update review in the database
            messagebox.showinfo("Success", "Performance review updated.")
            refresh_reviews()  # Refresh the review list
        except Exception as e:
            messagebox.showerror("Database Error", str(e))

    def delete_review():
        review_id = entry_delete_review_id.get()

        if not review_id:
            messagebox.showerror("Error", "Review ID is required!")
            return

        try:
            delete_performance_review(review_id)  # Delete review from the database
            messagebox.showinfo("Success", "Performance review deleted.")
            refresh_reviews()  # Refresh the review list
        except Exception as e:
            messagebox.showerror("Database Error", str(e))

    win = tk.Toplevel()
    win.title("Performance Reviews")
    win.geometry("600x600")

    tk.Label(win, text="Employee ID").pack()
    entry_emp_id = tk.Entry(win)
    entry_emp_id.pack()

    tk.Label(win, text="Review Date (YYYY-MM-DD)").pack()
    entry_review_date = tk.Entry(win)
    entry_review_date.pack()

    tk.Label(win, text="Comments").pack()
    entry_comments = tk.Entry(win)
    entry_comments.pack()

    tk.Label(win, text="Rating (1-5)").pack()
    entry_rating = tk.Entry(win)
    entry_rating.pack()

    tk.Button(win, text="Submit Review", command=submit_review).pack(pady=5)

    tk.Label(win, text="All Reviews").pack(pady=10)
    review_list = tk.Listbox(win, width=80)
    review_list.pack()

    tk.Button(win, text="Refresh Reviews", command=refresh_reviews).pack(pady=5)

    tk.Label(win, text="Update Review").pack(pady=10)
    tk.Label(win, text="Review ID").pack()
    entry_review_id = tk.Entry(win)
    entry_review_id.pack()

    tk.Label(win, text="New Comments").pack()
    entry_update_comments = tk.Entry(win)
    entry_update_comments.pack()

    tk.Label(win, text="New Rating (1-5)").pack()
    entry_update_rating = tk.Entry(win)
    entry_update_rating.pack()

    tk.Button(win, text="Update Review", command=update_review).pack(pady=5)

    tk.Label(win, text="Delete Review").pack(pady=10)
    tk.Label(win, text="Review ID").pack()
    entry_delete_review_id = tk.Entry(win)
    entry_delete_review_id.pack()

    tk.Button(win, text="Delete Review", command=delete_review).pack(pady=5)

    refresh_reviews()  # Load reviews when the window is opened

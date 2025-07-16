import tkinter as tk  # Import Tkinter for managing the main application window
from gui.login_window import login_screen
from gui.department_gui import add_department_gui, view_departments_gui
from gui.attendance_gui import mark_attendance_gui, view_attendance_gui, update_attendance_gui
from utils.db_connection import initialize_database

def launch_gui():
    """
    Launch the main GUI components of the application.
    """
    # Launch the login screen
    login_screen()

    # Example usage of other GUI functions
    mark_attendance_gui()
    view_attendance_gui()
    update_attendance_gui()
    add_department_gui()
    view_departments_gui()

    # Example call to update_employee with correct arguments
  
# Ensure no incorrect calls to add_employee are present
# If needed, call add_employee with the correct arguments elsewhere

if __name__ == "__main__":
    initialize_database()  # Ensure the database is initialized

    # Create the main Tkinter application window
    root = tk.Tk()
    root.withdraw()  # Hide the root window as it is not used directly

    # Launch the GUI
    launch_gui()

    # Start the Tkinter main loop
    root.mainloop()

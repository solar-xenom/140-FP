import tkinter as tk  # Import Tkinter for GUI management
from tkinter import messagebox  # Import messagebox for popup alerts

# Function to create and open a second window
def open_second_window():
    second_window = tk.Toplevel()  # Create a new top-level window
    second_window.title("Second Window")  # Set the window title
    second_window.geometry("300x200")  # Set the window size
    tk.Label(second_window, text="Welcome to the second window! Have a nice day!").pack()  # Display welcome message

# Function to validate user input in the entry field
def validate_input(entry):
    if not entry.get().strip():  # Check if the entry field is empty or contains only spaces
        messagebox.showerror("Input Error", "Entry cannot be empty!")  # Show error message
        return False  # Return validation failure
    messagebox.showinfo("Input Valid", "Entry is valid!")  # Show success message
    return True  # Return validation success

# Function to exit and close the application
def exit_app(root):
    root.destroy()  # Destroy the main application window

import tkinter as tk  # Import the Tkinter library for GUI creation
from tkinter import font  # Import font module for custom fonts
from functions import open_second_window, validate_input, exit_app  # Import functions from external module

# Create the main application window
root = tk.Tk()
root.title("Decal Business Application")  # Set the title of the application window
root.geometry("400x300")  # Set the window size

# Define a custom font for UI elements
custom_font = font.Font(family="Helvetica", size=12, weight="bold")

# Labels for user interface
tk.Label(root, text="Main Window", font=custom_font).pack()  # Title label for the main window
tk.Label(root, text="Enter your name:", font=custom_font).pack()  # Prompt for user input

# Entry field for user input
name_entry = tk.Entry(root, font=custom_font)  # Create an entry box for the user's name
name_entry.pack()

# Load images and display them with alternate text
image1 = tk.PhotoImage(file="image1.png")  # Load the first image
image2 = tk.PhotoImage(file="image2.png")  # Load the second image
tk.Label(root, image=image1, text="Image 1 Cats", compound="top", font=custom_font).pack()  # Display first image with text
tk.Label(root, image=image2, text="Image 2 Facts", compound="top", font=custom_font).pack()  # Display second image with text

# Buttons for user interaction
tk.Button(root, text="Open Second Window", command=open_second_window, font=custom_font).pack()  # Button to open a new window
tk.Button(root, text="Validate Input", command=lambda: validate_input(name_entry), font=custom_font).pack()  # Button to validate user input
tk.Button(root, text="Exit", command=lambda: exit_app(root), font=custom_font).pack()  # Button to exit the application

# Run the main event loop to keep the application active
root.mainloop()

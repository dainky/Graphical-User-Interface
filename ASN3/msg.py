import tkinter as tk
from tkinter import messagebox

# Create the main window
root = tk.Tk()
root.title("Tkinter Messagebox Example")
root.geometry("300x150")

# Function to be called when the button is clicked
def show_info_popup():
    # Display the message box
    messagebox.showinfo("Information", "This is an informational message!")

# Create a button that calls the show_info_popup function
button = tk.Button(root, text="Click for Info", command=show_info_popup)
button.pack(pady=20)

# Start the Tkinter main loop
root.mainloop()
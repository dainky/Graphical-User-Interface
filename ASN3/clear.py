import tkinter as tk

def clear_entry_field(entry_widget):
    """Deletes all characters in the entry box."""
    entry_widget.delete(0, tk.END) # Deletes from index 0 to the end

# --- Example Implementation ---
root = tk.Tk()
root.geometry("300x200")

# 1. Create the Entry widget
entry_field = tk.Entry(root, width=30)
entry_field.pack(pady=10)

# 2. Add some default text for testing
entry_field.insert(0, "Enter text here...")

# 3. Create a Button that calls the clear function
#    A lambda is used to pass the specific widget as an argument
clear_button = tk.Button(root, text="Clear Entry", command=lambda: clear_entry_field(entry_field))
clear_button.pack(pady=10)

root.mainloop()

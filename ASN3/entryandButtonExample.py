import tkinter as tk

# Function to be called when the button is clicked
def get_input_value():
    # Use the .get() method on the entry widget object
    user_input = entry_box.get()
    print(f"The user entered: {user_input}")

# --- Main application setup ---
window = tk.Tk()
window.title("Entry Input Example")

# 1. Create the Entry widget
# Keep a reference to the widget instance (entry_box)
entry_box = tk.Entry(window, width=50)
entry_box.pack(pady=10)

# 2. Create a Button to trigger the retrieval function
# The 'command' argument links the button to the function
submit_button = tk.Button(window, text="Submit", command=get_input_value)
submit_button.pack(pady=10)

# Run the Tkinter event loop
window.mainloop()


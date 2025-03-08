import tkinter as tk
import random

# Initialize the main application window
root = tk.Tk()
root.title("RF-Based Lost Item Tracker")
root.geometry("400x300")

# Label for selecting an item
label = tk.Label(root, text="Select Lost Item:")
label.pack()

# Dropdown menu for selecting an item
items = ["Keys", "Wallet", "Remote", "Glasses"]
selected_item = tk.StringVar(root)
selected_item.set(items[0])  # Default selection
item_menu = tk.OptionMenu(root, selected_item, *items)
item_menu.pack()

# Signal strength bar (simulating RF signal changes)
signal_bar = tk.Scale(root, from_=0, to=100, orient="horizontal", length=300, label="Signal Strength")
signal_bar.pack()

# Label to display the result
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack()

# Function to simulate signal strength changes
def track_item():
    signal_strength = random.randint(0, 100)
    signal_bar.set(signal_strength)
    
    if signal_strength > 70:
        result_label.config(text="You are very close! ✅", fg="green")
    elif 40 <= signal_strength <= 70:
        result_label.config(text="Getting closer... ⚠️", fg="orange")
    else:
        result_label.config(text="Still far away ❌", fg="red")

# Button to start tracking
track_button = tk.Button(root, text="Track Item", command=track_item)
track_button.pack()

# Run the Tkinter GUI
root.mainloop()

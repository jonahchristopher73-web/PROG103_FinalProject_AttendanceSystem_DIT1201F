import tkinter as tk
from tkinter import messagebox

# Dictionary to store attendance
records = {}

# Function to add a record
def add_record():
    name = name_entry.get()
    status = status_entry.get()
    if name != "" and status != "":
        records[name] = status
        messagebox.showinfo("Saved", f"{name} marked as {status}")
        name_entry.delete(0, tk.END)
        status_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Error", "Fill in both fields")

# Function to show all records
def show_records():
    output.delete("1.0", tk.END)
    for student in records:
        output.insert(tk.END, student + ": " + records[student] + "\n")

# Function to clear everything
def clear_records():
    records.clear()
    output.delete("1.0", tk.END)
    messagebox.showinfo("Cleared", "All records removed")

# Main window
root = tk.Tk()
root.title("Attendance System")

# Labels and inputs
tk.Label(root, text="Name").grid(row=0, column=0, padx=5, pady=5)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Status (Present/Absent)").grid(row=1, column=0, padx=5, pady=5)
status_entry = tk.Entry(root)
status_entry.grid(row=1, column=1, padx=5, pady=5)

# Buttons
tk.Button(root, text="Add", command=add_record).grid(row=2, column=0, pady=5)
tk.Button(root, text="Show", command=show_records).grid(row=2, column=1, pady=5)
tk.Button(root, text="Clear", command=clear_records).grid(row=3, column=0, pady=5)
tk.Button(root, text="Exit", command=root.quit).grid(row=3, column=1, pady=5)

# Output area
output = tk.Text(root, height=10, width=40)
output.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()

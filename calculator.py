 import tkinter as tk
from tkinter import messagebox


def on_click(button_text):
    if button_text == "=":
        try:
            result = eval(entry_var.get())
            entry_var.set(result)
        except Exception as e:
            messagebox.showerror("Error", "Invalid Expression")
    elif button_text == "C":
        entry_var.set("")
    else:
        entry_var.set(entry_var.get() + button_text)


# Create main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")

time_label = tk.Label(root, text="Basic Calculator", font=("Arial", 14))
time_label.pack()

entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, font=(
    "Arial", 18), justify='right', bd=10, relief=tk.RIDGE)
entry.pack(fill="both", padx=10, pady=10)

buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", "C", "=", "+"]
]

frame = tk.Frame(root)
frame.pack()

for row in buttons:
    button_row = tk.Frame(frame)
    button_row.pack(side=tk.TOP)
    for btn_text in row:
        button = tk.Button(button_row, text=btn_text, font=("Arial", 14), width=5, height=2,
                           command=lambda text=btn_text: on_click(text))
        button.pack(side=tk.LEFT, padx=5, pady=5)

root.mainloop()

run this file use this command python file_name.py  in  terminal  == python todo.py
import tkinter as tk
from tkinter import messagebox
import json
import os

TASKS_FILE = "tasks.json"


def load_tasks():
    if os.path.exists(TASKS_FILE):
        try:
            with open(TASKS_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            messagebox.showerror("Error", f"Error loading tasks: {e}")
            return []
    return []


def save_tasks(tasks):
    try:
        with open(TASKS_FILE, 'w', encoding='utf-8') as f:
            json.dump(tasks, f, indent=4)
    except Exception as e:
        messagebox.showerror("Error", f"Error saving tasks: {e}")


def add_task():
    task_text = entry_task.get().strip()
    if not task_text:
        messagebox.showwarning("Input Error", "Please enter a task.")
        return
    tasks.append({"task": task_text, "completed": False})
    update_task_list()
    entry_task.delete(0, tk.END)
    save_tasks(tasks)


def delete_task():
    selected = listbox_tasks.curselection()
    if not selected:
        messagebox.showwarning(
            "Selection Error", "Please select a task to delete.")
        return
    index = selected[0]
    tasks.pop(index)
    update_task_list()
    save_tasks(tasks)


def mark_completed():
    selected = listbox_tasks.curselection()
    if not selected:
        messagebox.showwarning(
            "Selection Error", "Please select a task to mark as completed.")
        return
    index = selected[0]
    tasks[index]["completed"] = True
    update_task_list()
    save_tasks(tasks)


def update_task_list():
    listbox_tasks.delete(0, tk.END)
    for task in tasks:
        display_text = task["task"]
        if task["completed"]:
            display_text += "  (Completed)"
        listbox_tasks.insert(tk.END, display_text)


def on_closing():
    save_tasks(tasks)
    root.destroy()


# Main window setup
root = tk.Tk()
root.title("To-Do List Application")
root.geometry("400x400")

# Load tasks from file
tasks = load_tasks()

# Entry and Add Button
frame_entry = tk.Frame(root)
frame_entry.pack(pady=10)
entry_task = tk.Entry(frame_entry, width=40)
entry_task.pack(side=tk.LEFT, padx=5)
button_add = tk.Button(frame_entry, text="Add Task", command=add_task)
button_add.pack(side=tk.LEFT, padx=5)

# Listbox to display tasks
listbox_tasks = tk.Listbox(root, width=50, height=15)
listbox_tasks.pack(pady=10)

# Delete and Mark Completed Buttons
frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=5)
button_delete = tk.Button(
    frame_buttons, text="Delete Task", command=delete_task)
button_delete.pack(side=tk.LEFT, padx=5)
button_mark = tk.Button(
    frame_buttons, text="Mark Completed", command=mark_completed)
button_mark.pack(side=tk.LEFT, padx=5)

# Update the listbox with current tasks
update_task_list()

# Ensure tasks are saved when closing the app
root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()

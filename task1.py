import tkinter as tk
from tkinter import messagebox
import json

tasks = []

def add_task():
    title = title_entry.get()
    description = description_entry.get()
    if title and description:
        task_id = len(tasks) + 1
        tasks.append({'id': task_id, 'title': title, 'description': description})
        update_task_list()
        title_entry.delete(0, tk.END)
        description_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please fill in both title and description")

def update_task():
    selected_task = task_listbox.curselection()
    if selected_task:
        index = selected_task[0]
        task = tasks[index]
        new_title = title_entry.get()
        new_description = description_entry.get()
        if new_title:
            task['title'] = new_title
        if new_description:
            task['description'] = new_description
        update_task_list()
    else:
        messagebox.showwarning("Selection Error", "Please select a task to update")

def delete_task():
    selected_task = task_listbox.curselection()
    if selected_task:
        index = selected_task[0]
        tasks.pop(index)
        update_task_list()
    else:
        messagebox.showwarning("Selection Error", "Please select a task to delete")

def update_task_list():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        task_listbox.insert(tk.END, f"{task['id']}: {task['title']} - {task['description']} ")

def save_tasks():
    with open('tasks_gui.json', 'w') as f:
        json.dump(tasks, f)

def load_tasks():
    global tasks
    try:
        with open('tasks_gui.json', 'r') as f:
            tasks = json.load(f)
        update_task_list()
    except FileNotFoundError:
        pass

app = tk.Tk()
app.title("To-Do List Application")
app.configure(bg="#f0f0f0")  # Change the background color

title_label = tk.Label(app, text="Title", font=('Arial', 14), bg="pink")
title_label.pack(pady=5)
title_entry = tk.Entry(app, font=('Arial', 14), width=40)
title_entry.pack(pady=5)

description_label = tk.Label(app, text="Description", font=('Arial', 14), bg="pink")
description_label.pack(pady=5)
description_entry = tk.Entry(app, font=('Arial', 14), width=40)
description_entry.pack(pady=5)

add_button = tk.Button(app, text="Add Task", command=add_task, font=('Arial', 12), width=15, bg="#d1e7dd")
add_button.pack(pady=5)

update_button = tk.Button(app, text="Update Task", command=update_task, font=('Arial', 12), width=15, bg="#d1e7dd")
update_button.pack(pady=5)

delete_button = tk.Button(app, text="Delete Task", command=delete_task, font=('Arial', 12), width=15, bg="#d1e7dd")
delete_button.pack(pady=5)

task_listbox = tk.Listbox(app, font=('Arial', 12), width=50, height=10)
task_listbox.pack(pady=10)

load_tasks()

app.protocol("WM_DELETE_WINDOW", lambda: (save_tasks(), app.destroy()))
app.mainloop()

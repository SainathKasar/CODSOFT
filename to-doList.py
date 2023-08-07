import tkinter as tk
from tkinter import messagebox
import json

class TodoList:
    def __init__(self, root):
        #root gemetry
        self.root = root
        self.root.title("To-Do Task List ")
        self.root.geometry("500x400")
        
        self.tasks = []
        self.load_tasks()
        #task entry
        self.task_entry = tk.Entry(root,width=40)
        self.task_entry.pack(pady=10, padx=10)
        #addButton
        add_button = tk.Button(root, text="Add Task", command=self.add_task)
        add_button.pack()
        #default listbox in tkinter
        self.task_listbox = tk.Listbox(root,width=40)
        self.task_listbox.pack(pady=10, padx=10, ipadx=5, ipady=5)
        #DoneButton
        mark_complete_button = tk.Button(root, text="Mark Completed", command=self.mark_completed)
        mark_complete_button.pack(pady=10, padx=10)
        #clearButton
        clear_button = tk.Button(root, text="Clear All Tasks", command=self.clear_tasks)
        clear_button.pack()

        self.update_task_listbox()

    def load_tasks(self):
        try:
            with open('Mytasks.json', 'r') as f:
                self.tasks = json.load(f)
        except FileNotFoundError:
            self.tasks = []

    def save_tasks(self):
        with open('Mytasks.json', 'w') as f:
            json.dump(self.tasks, f)

    def add_task(self):
        task_description = self.task_entry.get()
        if task_description:
            self.tasks.append({'description': task_description, 'completed': False})
            self.update_task_listbox()
            self.save_tasks()
            self.task_entry.delete(0, tk.END)

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for idx, task in enumerate(self.tasks):
            status = "✓" if task['completed'] else " "
            self.task_listbox.insert(tk.END, f"{idx + 1}. [{status}] {task['description']}")

    def mark_completed(self):
        selected_indices = self.task_listbox.curselection()
        for index in selected_indices:
            task_index = int(index)
            self.tasks[task_index]['completed'] = True
        self.update_task_listbox()
        self.save_tasks()

    # Add this method to the TodoApp class
    def clear_tasks(self):
        self.tasks.clear()
        self.update_task_listbox()
        self.save_tasks()


if __name__ == "__main__":
    root = tk.Tk()
    TDL = TodoList(root)
    root.mainloop()


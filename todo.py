import json
import os
import tkinter as tk
from tkinter import messagebox, simpledialog

# File to store tasks
TASKS_FILE = 'tasks.json'


class Task:
    def __init__(self, title, description='', due_date=None, priority='Normal'):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.completed = False

    def to_dict(self):
        return {
            'title': self.title,
            'description': self.description,
            'due_date': self.due_date,
            'priority': self.priority,
            'completed': self.completed
        }

    @staticmethod
    def from_dict(data):
        task = Task(
            title=data['title'],
            description=data['description'],
            due_date=data.get('due_date'),
            priority=data.get('priority', 'Normal')
        )
        task.completed = data.get('completed', False)
        return task


class TodoList:
    def __init__(self):
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if os.path.exists(TASKS_FILE):
            with open(TASKS_FILE, 'r') as file:
                tasks_data = json.load(file)
                return [Task.from_dict(task) for task in tasks_data]
        return []

    def save_tasks(self):
        with open(TASKS_FILE, 'w') as file:
            json.dump([task.to_dict() for task in self.tasks], file)

    def add_task(self, task):
        self.tasks.append(task)
        self.save_tasks()

    def update_task(self, index, title=None, description=None, due_date=None, priority=None):
        if 0 <= index < len(self.tasks):
            if title:
                self.tasks[index].title = title
            if description:
                self.tasks[index].description = description
            if due_date:
                self.tasks[index].due_date = due_date
            if priority:
                self.tasks[index].priority = priority
            self.save_tasks()

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            self.save_tasks()

    def mark_complete(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].completed = True
            self.save_tasks()


class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        self.todo_list = TodoList()

        self.task_listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=50, height=15)
        self.task_listbox.pack(pady=10)

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=5)

        self.update_button = tk.Button(root, text="Update Task", command=self.update_task)
        self.update_button.pack(pady=5)

        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(pady=5)

        self.complete_button = tk.Button(root, text="Mark Complete", command=self.mark_complete)
        self.complete_button.pack(pady=5)

        self.load_tasks()

    def load_tasks(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.todo_list.tasks:
            status = "✓" if task.completed else "✗"
            self.task_listbox.insert(tk.END, f"[{status}] {task.title} (Priority: {task.priority}, Due: {task.due_date})")

    def add_task(self):
        title = simpledialog.askstring("Task Title", "Enter task title:")
        if title:
            description = simpledialog.askstring("Task Description", "Enter task description (optional):")
            due_date = simpledialog.askstring("Due Date", "Enter due date (YYYY-MM-DD, optional):")
            priority = simpledialog.askstring("Priority", "Enter priority (Low, Normal, High):")
            task = Task(title, description, due_date, priority)
            self.todo_list.add_task(task)
            self.load_tasks()

    def update_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            title = simpledialog.askstring("Update Task", "Enter new title (leave blank to keep current):")
            description = simpledialog.askstring("Update Task", "Enter new description (leave blank to keep current):")
            due_date = simpledialog.askstring("Update Task", "Enter new due date (leave blank to keep current):")
            priority = simpledialog.askstring("Update Task", "Enter new priority (leave blank to keep current):")
            self.todo_list.update_task(index, title or None, description or None, due_date or None, priority or None)
            self.load_tasks()
        else:
            messagebox.showwarning("Update Task", "Please select a task to update.")

    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            self.todo_list.delete_task(index)
            self.load_tasks()
        else:
            messagebox.showwarning("Delete Task", "Please select a task to delete.")

    def mark_complete(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            self.todo_list.mark_complete(index)
            self.load_tasks()
        else:
            messagebox.showwarning("Complete Task", "Please select a task to mark as complete.")


if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
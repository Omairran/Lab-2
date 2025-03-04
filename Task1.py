import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("400x400")

        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.pack(pady=10)

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack()

        self.remove_button = tk.Button(root, text="Remove Selected", command=self.remove_task)
        self.remove_button.pack()

        self.task_list = tk.Listbox(root, width=50, height=15)
        self.task_list.pack(pady=10)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.task_list.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Task cannot be empty!")

    def remove_task(self):
        try:
            selected_index = self.task_list.curselection()[0]
            self.task_list.delete(selected_index)
        except IndexError:
            messagebox.showwarning("Warning", "No task selected!")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()

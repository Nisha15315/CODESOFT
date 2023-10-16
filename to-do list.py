Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import tkinter as tk
... 
... class ToDoListApp:
...     def __init__(self):
...         self.window = tk.Tk()
...         self.window.title("To-Do List")
... 
...         # Create a listbox to store the to-do items
...         self.task_listbox = tk.Listbox(self.window)
...         self.task_listbox.pack()
... 
...         # Create a button to add a new to-do item
...         self.add_task_button = tk.Button(self.window, text="Add Task", command=self.add_task)
...         self.add_task_button.pack()
... 
...         # Create a button to mark a to-do item as complete
...         self.complete_task_button = tk.Button(self.window, text="Complete Task", command=self.complete_task)
...         self.complete_task_button.pack()
... 
...         # Create a button to delete a to-do item
...         self.delete_task_button = tk.Button(self.window, text="Delete Task", command=self.delete_task)
...         self.delete_task_button.pack()
... 
...         # Start the mainloop
...         self.window.mainloop()
... 
...     def add_task(self):
...         # Get the new to-do item from the user
...         new_task = tk.simpledialog.askstring("Add Task", "What is the new to-do item?")
... 
...         # Add the new to-do item to the listbox
...         self.task_listbox.insert('end', new_task)
... 
    def complete_task(self):
        # Get the index of the to-do item to complete
        selected_index = self.task_listbox.curselection()

        # Delete the to-do item from the listbox
        self.task_listbox.delete(selected_index)

    def delete_task(self):
        # Get the index of the to-do item to delete
        selected_index = self.task_listbox.curselection()

        # Delete the to-do item from the listbox
        self.task_listbox.delete(selected_index)

if __name__ == "__main__":

import tkinter as tk

def add_task():
    task = entry_task.get()
    if task:
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)

def remove_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
    except IndexError:
        pass

def complete_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.itemconfig(task_index, {'bg': 'light gray'})
    except IndexError:
        pass

# Create the main window
root = tk.Tk()
root.title("To-Do List")

# Set the icon
root.iconbitmap('ico.ico')  # Change 'icon.ico' to the path of your icon file

# Create and pack the necessary widgets
frame_tasks = tk.Frame(root)
frame_tasks.pack()

listbox_tasks = tk.Listbox(frame_tasks, height=10, width=50)
listbox_tasks.pack(side=tk.LEFT)

scrollbar_tasks = tk.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.Y)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

entry_task = tk.Entry(root, width=50)
entry_task.pack()

button_add_task = tk.Button(root, text="Add Task", width=48, command=add_task)
button_add_task.pack()

button_remove_task = tk.Button(root, text="Remove Task", width=48, command=remove_task)
button_remove_task.pack()

button_complete_task = tk.Button(root, text="Complete Task", width=48, command=complete_task)
button_complete_task.pack()

root.mainloop()

from tkinter import *

tasks = []

def display_menu():
    print("**Menu**")
    print("1. Add task")
    print("2. View task")
    print("3. Mark as Done")
    print("4. Exit")

def add_task():
    task = task_entry.get()
    if task:
        tasks.append(task)
        task_entry.delete(0, END)
        view_task()
        print("Task added successfully")
    else:
        print("Please enter a task")
    save_task()

def view_task():
    tasks_text.delete(1.0, END)
    tasks_text.insert(END, "**Tasks**\n")
    for i, task in enumerate(tasks, start=1):
        tasks_text.insert(END, f"{i}. {task}\n")

def delete_task():
    index = int(index_entry.get()) - 1
    index_entry.delete(0, END)

    if 0 <= index < len(tasks):
        removed_task = tasks.pop(index)
        view_task()
        print(f"Task '{removed_task}' marked as done and removed")
    else:
        print("Invalid task index")
    save_task

def save_task():
    try:
        with open("text.txt", "w") as f:
            for task in tasks:
                f.write(task + '\n')
            print("Tasks saved successfully")
    except Exception as e:
        print("Error while saving tasks:", str(e))

def load_tasks():
    global tasks
    tasks = []
    try:
        with open("text.txt", "r") as f:
            tasks = f.read().splitlines()
        print("Tasks loaded successfully")
    except FileNotFoundError:
        print("No saved tasks found")

def main():
    global tasks, task_entry, tasks_text, index_entry

    load_tasks()

    root = Tk()
    root.geometry('500x500+450+100')
    root.config(bg="#33FFA4")
    root.title("TO-DO-LIST")
    root.resizable(width=False,height=False)

    frame = Frame(root)
    frame.pack(fill=X)
    Button(frame, text="View", font=("Times new roman", 12), bg="#D6FF33",command=view_task).pack(side=LEFT)
    Button(frame, text="Exit", font=("Times new roman", 12), bg="#D6FF33",command=root.quit).pack(side=LEFT)

    tasks_text = Text(root,height=10,width=40, pady=10,fg="#464646",selectbackground="#a6a6a6",highlightthickness=0)
    tasks_text.pack()
    tasks_text.insert("1.0","Click on 'View' Tab to show all your To-do-list")

    Label(root, text="Enter the task", font=("Times", 15)).pack()
    task_entry = Entry(root, width=50)
    task_entry.pack()

    Button(root, text="Add Task", command=add_task,bg="green", font=('Times', 15)).pack(pady=5)

    Label(root,text="Enter the index number to delete the task",font=("Times",15)).pack()
    remove=Frame(root)
    Label(remove, text="Enter the index", font=("Times", 15)).pack()
    index_entry = Entry(root, width=30)
    index_entry.pack()

    Button(root, text="Delete", command=delete_task,bg="red", font=('Times', 15)).pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()

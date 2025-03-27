from tkinter import *
from tkinter import font
import sqlite3

root_window = Tk()
root_window.geometry("800x600")
root_window.configure(bg="#DACEC4")
root_window.title("To-Do List Desktop")

# configure the grid
root_window.columnconfigure(1, weight=1)

mainPglabel = Label(root_window, text = "Welcome to Task Manager", font = font.Font(size=24))
mainPglabel.grid(column=0, row=0, columnspan=2, pady=10)

frame = Frame(root_window)
frame.grid(column=1, row=2, padx=10, pady=10, sticky='N')

task_entry= Entry(root_window, text="Task")
task_entry.grid(column=1, row=3, sticky='' , padx=5, pady=5)

description_entry= Entry(root_window, text="Description")
description_entry.grid(column=1, row=4, sticky='' , padx=5, pady=5)

submit_button = Button(root_window, text="Submit", command=lambda: add_task(task_entry.get(), description_entry.get()))
submit_button.grid(column=1, row=5, sticky='' , padx=5, pady=5)


theList = Listbox(frame, 
        width= 35,
        height= 10,
        bg="SystemButtonFace",
        bd= 0,
        fg= "#464646"
        )
theList.pack()


dataConnector = sqlite3.connect("toDo.db")
cursor = dataConnector.cursor()

# if the table does not exist, create it
listOfTables = cursor.execute(
    "SELECT name FROM sqlite_master WHERE type='table' AND name='Tasks'"
).fetchall()
if listOfTables == []:
    cursor.execute(""" CREATE TABLE Tasks (
        task_name   text,
        description text,
        status      text,
        due_date    text,
        involved    text
    )""")
dataConnector.commit()
dataConnector.close()

# FUNCTIONS
def query_tasks():
    dataConnector = sqlite3.connect("toDo.db")
    cursor = dataConnector.cursor()

    cursor.execute("SELECT * FROM tasks")
    tasklist = cursor.fetchall()

    theList.delete(0, END)

    for task in tasklist:
        theList.insert(END, f"{task[0]} , {task[1]}")

    # itr = 0
    # for task in tasklist:
    #     temp = Label(root_window, text=task)
    #     temp.grid(row=itr, column=1)
    #     itr += 1
    dataConnector.close()

def add_task(task, description):
    """Insert a new task into the database and refresh the task list."""
    if task.strip() == "":  # Prevent empty tasks
        return

    dataConnector = sqlite3.connect("toDo.db")
    cursor = dataConnector.cursor()

    try:
        cursor.execute("INSERT INTO Tasks (task_name, description, status, due_date, involved) VALUES (?, ?, '', '', '')", (task,description))
        dataConnector.commit()
    except sqlite3.IntegrityError:
        print("Task already exists!")  # Avoid duplicate tasks

    dataConnector.close()
    task_entry.delete(0, END)
    description_entry.delete(0, END)
    query_tasks()

def login():
    label_font = font.Font(size = 24)
    signInlabel = Label(root_window, text = "Sign In Page", font = label_font)
    signInlabel.grid(column=0, row=0, columnspan=2, pady=10)

    user_label = Label(root_window, text = "Username: ")
    user_label.grid(column=0, row=1, sticky='W' , padx=5, pady=5)

    user_entry = Entry(root_window)
    user_entry.grid(column=1, row=1, sticky='W' , padx=5, pady=5)

    password_label = Label(root_window, text="Password: ")
    password_label.grid(column=0, row=2, sticky='W', padx=5, pady=5)

    password_entry = Entry(root_window, show="*")
    password_entry.grid(column=1, row=2, sticky='W' , padx=5, pady=5)

    login_button = Button(root_window, text="Login")
    login_button.grid(column=1, row=3, sticky='W' , padx=5, pady=5)
# MAKING WIDGETS

query_tasks()
# CALLING WIDGETS

root_window.mainloop()
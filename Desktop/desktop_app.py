from tkinter import *
import sqlite3

root_window = Tk()
root_window.geometry("800x600")
root_window.configure(bg="#DACEC4")
root_window.title("To-Do List Application")

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


# FUNCTIONS
def query_tasks():
    dataConnector = sqlite3.connect("toDo.db")
    cursor = dataConnector.cursor()

    cursor.execute("SELECT * FROM tasks")
    tasklist = cursor.fetchall()

    itr = 0
    for task in tasklist:
        temp = Label(root_window, text=task)
        temp.grid(row=itr, column=1)
        itr += 1


# MAKING WIDGETS

query_tasks()
# CALLING WIDGETS


root_window.mainloop()

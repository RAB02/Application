import tkinter.messagebox
from tkinter import END
import sqlite3


# Clears the screen so that we can show another frame
def clear_screen(frame):
    frame.pack_forget()
    return


# Makes pop-up window
def pop_up(error):
    tkinter.messagebox.showinfo("ERROR", error)


# Clears the fields from the input
def clear_fields(task, description, status, due_date, involved):
    task.delete(0, END)
    description.delete(0, END)
    status.delete(0, END)
    due_date.delete(0, END)
    involved.delete(0, END)


def query_users(uList):
    dataConnector = sqlite3.connect("toDo.db")
    cursor = dataConnector.cursor()

    cursor.execute("SELECT uID, first_name, last_name FROM Users WHERE admin = 0")
    normUsers = cursor.fetchall()

    for user in normUsers:
        uList.insert(END, f"{user[0]}: {user[1]} {user[2]}")

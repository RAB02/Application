from tkinter import Frame, Label, Button
from . import misc, main_page, root_window
import sqlite3


def go_back(user):
    if user[3] == 1:
        main_page.admin_page(user)
    else:
        main_page.main_page(user)


def task_screen(task, user):
    # Finding the users involved in task
    if len(task[5]) > 1:
        usrInvolved = task[5].split(",")
        queryString = "SELECT first_name, last_name FROM Users WHERE uID = ?"
        for i in range(len(usrInvolved) - 1):
            queryString = queryString + " OR uID = ?"
    else:
        usrInvolved = task[5]
        queryString = "SELECT first_name, last_name FROM Users WHERE uID = ?"

    dataConnector = sqlite3.connect("toDo.db")
    cursor = dataConnector.cursor()

    cursor.execute(queryString, usrInvolved)
    # Names come in tuples
    namesTup = cursor.fetchall()
    names = []
    for tup in namesTup:
        names.append(" ".join(tup))
    namesInv = ",".join(names)

    dataConnector.close()
    # MAKING WIDGETS
    frame = Frame(root_window.root_window, bg="#DACEC4")
    mainPglabel = Label(frame, text="Task Info", font=("", 24), bg="#DACEC4")
    info_frame = Frame(frame, bg="#DACEC4")
    task_id = Label(info_frame, font=("", 15), text=f"Task ID: {task[0]}", bg="#DACEC4")
    task_name = Label(
        info_frame, font=("", 15), text=f"Task Name: {task[1]}", bg="#DACEC4"
    )
    task_desc = Label(
        info_frame, font=("", 15), text=f"Task Description: {task[2]}", bg="#DACEC4"
    )
    task_status = Label(
        info_frame, font=("", 15), text=f"Task Status: {task[3]}", bg="#DACEC4"
    )
    task_due = Label(
        info_frame, font=("", 15), text=f"Task Due Date: {task[4]}", bg="#DACEC4"
    )
    task_involved = Label(
        info_frame, font=("", 15), text=f"Users Involved: {namesInv}", bg="#DACEC4"
    )
    back = Button(
        frame,
        text="Back",
        command=lambda: [misc.clear_screen(frame), go_back(user)],
    )

    # CALLING WIDGETS
    frame.pack(anchor="center", padx=10, pady=10, expand=True)
    mainPglabel.pack(side="top", pady=10)
    info_frame.pack()
    task_id.pack()
    task_name.pack()
    task_desc.pack()
    task_status.pack()
    task_due.pack()
    task_involved.pack()
    back.pack()

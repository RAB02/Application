from tkinter import Frame, Label, Button
from . import misc, main_page, root_window


def task_screen(task, user):
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
        info_frame, font=("", 15), text=f"Users Involved: {task[5]}", bg="#DACEC4"
    )
    back = Button(
        frame,
        text="Back",
        command=lambda: [misc.clear_screen(frame), main_page.main_page(user)],
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

from tkinter import Frame, Label, Entry, Button, LEFT, RIGHT, Listbox
from . import misc, task_management, login, root_window


def admin_page(user):
    # MAKING WIDGETS
    frame = Frame(root_window.root_window, bg="#DACEC4")
    welcomeStr = "Hello " + user[1] + " " + user[2]
    welcomeLabel = Label(frame, text=welcomeStr, font=("", 20), bg="#DACEC4")
    logout = Button(
        frame, text="Log Out", command=lambda: [misc.clear_screen(frame), login.login()]
    )
    mainPglabel = Label(
        frame, text="Welcome to Task Manager", font=("", 24), bg="#DACEC4"
    )
    input_frame = Frame(frame, bg="#DACEC4")

    name_frame = Frame(input_frame, bg="#DACEC4")
    task_entry = Entry(name_frame)
    task_label = Label(name_frame, text="Task Name: ", bg="#DACEC4")

    desc_frame = Frame(input_frame, bg="#DACEC4")
    description_entry = Entry(desc_frame)
    description_label = Label(desc_frame, text="Task Description: ", bg="#DACEC4")

    status_frame = Frame(input_frame, bg="#DACEC4")
    status_entry = Entry(status_frame)
    status_label = Label(status_frame, text="Task Status: ", bg="#DACEC4")

    due_frame = Frame(input_frame, bg="#DACEC4")
    due_entry = Entry(due_frame)
    due_label = Label(due_frame, text="Task Due Date: ", bg="#DACEC4")

    involved_frame = Frame(input_frame, bg="#DACEC4")
    involved_entry = Entry(involved_frame)
    involved_label = Label(involved_frame, text="Users Involved: ", bg="#DACEC4")

    submit_button = Button(
        frame,
        text="Submit",
        command=lambda: [
            task_management.add_task(
                task_entry.get(),
                description_entry.get(),
                status_entry.get(),
                due_entry.get(),
                involved_entry.get(),
                theList,
                user,
            ),
            misc.clear_fields(
                task_entry, description_entry, status_entry, due_entry, involved_entry
            ),
        ],
    )
    go_button = Button(
        frame,
        text="See Task",
        command=lambda: [
            misc.clear_screen(frame),
            task_management.selected_item(theList, user),
        ],
    )

    delete_button = Button(
        frame,
        text="Delete Task",
        command=lambda: [task_management.delete_task(theList, user)],
    )

    theList = Listbox(
        frame,
        width=35,
        height=10,
        bg="SystemButtonFace",
        bd=0,
        fg="#464646",
        selectmode="single",
    )

    # CALLING WIDGETS
    logout.pack()
    welcomeLabel.pack(side="top", pady=10)
    frame.pack(anchor="center", padx=10, pady=10)
    mainPglabel.pack(side="top", pady=10)
    theList.pack(fill="both")

    input_frame.pack()
    name_frame.pack()
    task_entry.pack(pady=10, side=RIGHT)
    task_label.pack(side=LEFT)

    desc_frame.pack()
    description_entry.pack(pady=5, padx=5, side=RIGHT)
    description_label.pack(side=LEFT)

    status_frame.pack()
    status_entry.pack(pady=5, padx=5, side=RIGHT)
    status_label.pack(side=LEFT)

    due_frame.pack()
    due_entry.pack(pady=5, padx=5, side=RIGHT)
    due_label.pack(side=LEFT)

    involved_frame.pack()
    involved_entry.pack(pady=5, padx=5, side=RIGHT)
    involved_label.pack(side=LEFT)

    go_button.pack(padx=5, pady=5)
    delete_button.pack(padx=5, pady=5)
    submit_button.pack(padx=5, pady=5)
    task_management.query_tasks(theList, user)


def main_page(user):
    # MAKING WIDGETS
    frame = Frame(root_window.root_window, bg="#DACEC4")
    welcomeStr = "Hello " + user[1] + " " + user[2]
    welcomeLabel = Label(frame, text=welcomeStr, font=("", 20), bg="#DACEC4")
    logout = Button(
        frame, text="Log Out", command=lambda: [misc.clear_screen(frame), login.login()]
    )
    mainPglabel = Label(
        frame, text="Welcome to Task Manager", font=("", 24), bg="#DACEC4"
    )
    """
    input_frame = Frame(frame, bg="#DACEC4")

    name_frame = Frame(input_frame, bg="#DACEC4")
    task_entry = Entry(name_frame)
    task_label = Label(name_frame, text="Task Name: ", bg="#DACEC4")

    desc_frame = Frame(input_frame, bg="#DACEC4")
    description_entry = Entry(desc_frame)
    description_label = Label(desc_frame, text="Task Description: ", bg="#DACEC4")

    status_frame = Frame(input_frame, bg="#DACEC4")
    status_entry = Entry(status_frame)
    status_label = Label(status_frame, text="Task Status: ", bg="#DACEC4")

    due_frame = Frame(input_frame, bg="#DACEC4")
    due_entry = Entry(due_frame)
    due_label = Label(due_frame, text="Task Due Date: ", bg="#DACEC4")

    involved_frame = Frame(input_frame, bg="#DACEC4")
    involved_entry = Entry(involved_frame)
    involved_label = Label(involved_frame, text="Users Involved: ", bg="#DACEC4")

    submit_button = Button(
        frame,
        text="Submit",
        command=lambda: [
            task_management.add_task(
                task_entry.get(),
                description_entry.get(),
                status_entry.get(),
                due_entry.get(),
                involved_entry.get(),
                theList,
            ),
            misc.clear_fields(
                task_entry, description_entry, status_entry, due_entry, involved_entry
            ),
        ],
    )
    """
    go_button = Button(
        frame,
        text="See Task",
        command=lambda: [
            misc.clear_screen(frame),
            task_management.selected_item(theList, user),
        ],
    )
    """
    delete_button = Button(
        frame,
        text="Delete Task",
        command=lambda: [task_management.delete_task(theList)],
    )
    """
    theList = Listbox(
        frame,
        width=35,
        height=10,
        bg="SystemButtonFace",
        bd=0,
        fg="#464646",
        selectmode="single",
    )

    # CALLING WIDGETS
    logout.pack()
    welcomeLabel.pack(side="top", pady=10)
    frame.pack(anchor="center", padx=10, pady=10)
    mainPglabel.pack(side="top", pady=10)
    theList.pack(fill="both")

    """
    input_frame.pack()
    name_frame.pack()
    task_entry.pack(pady=10, side=RIGHT)
    task_label.pack(side=LEFT)

    desc_frame.pack()
    description_entry.pack(pady=5, padx=5, side=RIGHT)
    description_label.pack(side=LEFT)

    status_frame.pack()
    status_entry.pack(pady=5, padx=5, side=RIGHT)
    status_label.pack(side=LEFT)

    due_frame.pack()
    due_entry.pack(pady=5, padx=5, side=RIGHT)
    due_label.pack(side=LEFT)

    involved_frame.pack()
    involved_entry.pack(pady=5, padx=5, side=RIGHT)
    involved_label.pack(side=LEFT)
    """
    go_button.pack(padx=5, pady=5)
    # delete_button.pack(padx=5, pady=5)
    # submit_button.pack(padx=5, pady=5)
    task_management.query_tasks(theList, user)

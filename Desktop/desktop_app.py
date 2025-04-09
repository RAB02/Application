from tkinter import *
import tkinter.messagebox
import sqlite3

root_window = Tk()
root_window.geometry("800x600")
root_window.configure(bg="#DACEC4")
root_window.title("To-Do List Desktop")


dataConnector = sqlite3.connect("toDo.db")
cursor = dataConnector.cursor()

# if the table does not exist, create it
listOfTables = cursor.execute(
    "SELECT name FROM sqlite_master WHERE type='table' AND name='SignIn'"
).fetchall()
if listOfTables == []:
    cursor.execute(""" CREATE TABLE SignIn (
        sID         integer,
        username    text,
        password    text,
        PRIMARY KEY(sID AUTOINCREMENT)
    )""")

listOfTables = cursor.execute(
    "SELECT name FROM sqlite_master WHERE type='table' AND name='Users'"
).fetchall()
if listOfTables == []:
    cursor.execute(""" CREATE TABLE Users (
        uID         integer,
        first_name  text,
        last_name   text,
        admin       integer,
        PRIMARY KEY(uID),
        FOREIGN KEY(uID) REFERENCES SignIn(sID)
    )""")

listOfTables = cursor.execute(
    "SELECT name FROM sqlite_master WHERE type='table' AND name='Tasks'"
).fetchall()
if listOfTables == []:
    cursor.execute(""" CREATE TABLE Tasks (
        tID         integer,
        task_name   text,
        description text,
        status      text,
        due_date    text,
        involved    integer,
        PRIMARY KEY(tID AUTOINCREMENT),
        FOREIGN KEY(involved) REFERENCES Users(uID)
    )""")

dataConnector.commit()
dataConnector.close()


### FUNCTIONS ###


# queries tasks from database and displays them in the list
def query_tasks(theList):
    dataConnector = sqlite3.connect("toDo.db")
    cursor = dataConnector.cursor()

    cursor.execute("SELECT * FROM tasks")
    tasklist = cursor.fetchall()

    theList.delete(0, END)

    for task in tasklist:
        theList.insert(END, f"{task[0]}: {task[1]}")

    # itr = 0
    # for task in tasklist:
    #     temp = Label(root_window, text=task)
    #     temp.grid(row=itr, column=1)
    #     itr += 1
    dataConnector.close()


# adds a task to the given list
def add_task(task, description, status, due_date, theList):
    """Insert a new task into the database and refresh the task list."""
    if task.strip() == "":  # Prevent empty tasks
        return

    dataConnector = sqlite3.connect("toDo.db")
    cursor = dataConnector.cursor()

    try:
        cursor.execute(
            "INSERT INTO Tasks (task_name, description, status, due_date, involved) VALUES (?, ?, ?, ?, 0)",
            (task, description, status, due_date),
        )
        dataConnector.commit()
    except sqlite3.IntegrityError:
        print("Task already exists!")  # Avoid duplicate tasks

    dataConnector.close()
    query_tasks(theList)


# Makes pop-up window
def pop_up(error):
    tkinter.messagebox.showinfo("ERROR", error)

# Clears the fields from the input
def clear_fields(task, description, status, due_date):
    task.delete(0, END)
    description.delete(0, END)
    status.delete(0, END)
    due_date.delete(0, END)


# Clears the screen so that we can show another frame
def clear_screen(frame):
    frame.pack_forget()
    return


# Makes sure there is a valid login
def check_login(username, password, frame):
    dataConnector = sqlite3.connect("toDo.db")
    cursor = dataConnector.cursor()

    cursor.execute(
        "SELECT * FROM SignIn WHERE username = ? AND password = ?", [username, password]
    )
    if cursor.fetchall():
        clear_screen(frame)
        main_page()

    else:
        pop_up("INVALID LOG IN")
    return


# Calls the Login screen
def login():
    # MAKING WIDGETS
    login_frame = Frame(root_window, bg="#DACEC4")
    user_frame = Frame(login_frame, bg="#DACEC4")
    signInlabel = Label(login_frame, text="Sign In Page", bg="#DACEC4", font=("", 24))
    user_label = Label(user_frame, text="Username: ", bg="#DACEC4")
    user_entry = Entry(user_frame)
    password_frame = Frame(login_frame, bg="#DACEC4")
    password_label = Label(password_frame, text="Password: ", bg="#DACEC4")
    password_entry = Entry(password_frame, show="*")
    login_button = Button(
        login_frame,
        text="Login",
        command=lambda: check_login(
            user_entry.get(), password_entry.get(), login_frame
        ),
    )

    # CALLING WIDGETS
    login_frame.pack(anchor="center", pady=10, expand=True)
    signInlabel.pack(pady=10)
    user_frame.pack()
    password_frame.pack()
    user_label.pack(side=LEFT, padx=5, pady=5)
    user_entry.pack(side=RIGHT, padx=5, pady=5)
    password_label.pack(side=LEFT, padx=5, pady=5)
    password_entry.pack(side=RIGHT, padx=5, pady=5)
    login_button.pack(anchor="center")


# returns the task that is selected by mouse from the given list
def selected_item(list):
    try:
        id = int(list.get(list.curselection()[0])[0])
        dataConnector = sqlite3.connect("toDo.db")
        cursor = dataConnector.cursor()

        cursor.execute("SELECT * FROM tasks WHERE tID = ?", [id])
        task = cursor.fetchone()

        task_screen(task)

        dataConnector.close()
    except:
        error = "INVALID TASK SELECTED"
        main_page()
        pop_up(error)
        return


def main_page():
    # MAKING WIDGETS
    frame = Frame(root_window, bg="#DACEC4")
    logout = Button(
        frame, text="Log Out", command=lambda: [clear_screen(frame), login()]
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

    submit_button = Button(
        frame,
        text="Submit",
        command=lambda: [
            add_task(
                task_entry.get(),
                description_entry.get(),
                status_entry.get(),
                due_entry.get(),
                theList,
            ),
            clear_fields(task_entry, description_entry, status_entry, due_entry),
        ],
    )
    go_button = Button(
        frame,
        text="See Task",
        command=lambda: [clear_screen(frame), selected_item(theList)],
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

    go_button.pack(padx=5, pady=5)
    submit_button.pack(padx=5, pady=5)
    query_tasks(theList)


def task_screen(task):
    # MAKING WIDGETS
    frame = Frame(root_window, bg="#DACEC4")
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
    back = Button(
        frame, text="Back", command=lambda: [clear_screen(frame), main_page()]
    )

    # CALLING WIDGETS
    frame.pack(anchor="center", padx=10, pady=10, expand=True)
    mainPglabel.pack(side="top", pady=10)
    info_frame.pack()
    task_id.pack()
    task_name.pack()
    task_desc.pack()
    task_status.pack()
    back.pack()


# we only call login screen because
# it is the first screen the user will see.
login()

root_window.mainloop()

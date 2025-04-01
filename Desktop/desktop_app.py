from tkinter import *
import sqlite3

root_window = Tk()
root_window.geometry("800x600")
root_window.configure(bg="#DACEC4")
root_window.title("To-Do List Desktop")

# configure the grid
# root_window.columnconfigure(1, weight=1)


# mainPglabel.grid(column=0, row=0, columnspan=2, pady=10)
# frame.grid(column=1, row=2, padx=10, pady=10, sticky="N")
# task_entry.grid(column=1, row=3, sticky="", padx=5, pady=5)
# description_entry.grid(column=1, row=4, sticky="", padx=5, pady=5)
# submit_button.grid(column=1, row=5, sticky="", padx=5, pady=5)

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


# FUNCTIONS
def query_tasks(theList):
    dataConnector = sqlite3.connect("toDo.db")
    cursor = dataConnector.cursor()

    cursor.execute("SELECT * FROM tasks")
    tasklist = cursor.fetchall()

    theList.delete(0, END)

    for task in tasklist:
        theList.insert(END, f"{task[1]} , {task[2]}")

    # itr = 0
    # for task in tasklist:
    #     temp = Label(root_window, text=task)
    #     temp.grid(row=itr, column=1)
    #     itr += 1
    dataConnector.close()


def add_task(task, description, theList):
    """Insert a new task into the database and refresh the task list."""
    if task.strip() == "":  # Prevent empty tasks
        return

    dataConnector = sqlite3.connect("toDo.db")
    cursor = dataConnector.cursor()

    try:
        cursor.execute(
            "INSERT INTO Tasks (task_name, description, status, due_date, involved) VALUES (?, ?, '', '', '')",
            (task, description),
        )
        dataConnector.commit()
    except sqlite3.IntegrityError:
        print("Task already exists!")  # Avoid duplicate tasks

    dataConnector.close()
    # task_entry.delete(0, END)
    # description_entry.delete(0, END)
    query_tasks(theList)


def clear_fields(task, description):
    task.delete(0, END)
    description.delete(0, END)


def clear_screen(frame):
    frame.pack_forget()
    return


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
        print("WRONG LOGIN")

    return


def login():
    login_frame = Frame(root_window, bg="#DACEC4")
    login_frame.tkraise()
    user_frame = Frame(login_frame)
    signInlabel = Label(login_frame, text="Sign In Page", font=("", 24))
    user_label = Label(user_frame, text="Username: ")
    user_entry = Entry(user_frame)
    password_frame = Frame(login_frame)
    password_label = Label(password_frame, text="Password: ")
    password_entry = Entry(password_frame, show="*")
    login_button = Button(
        login_frame,
        text="Login",
        command=lambda: check_login(
            user_entry.get(), password_entry.get(), login_frame
        ),
    )

    login_frame.pack(anchor="center", pady=10, expand=True)
    signInlabel.pack(pady=10)
    user_frame.pack()
    password_frame.pack()
    user_label.pack(side=LEFT, padx=5, pady=5)
    user_entry.pack(side=RIGHT, padx=5, pady=5)
    password_label.pack(side=LEFT, padx=5, pady=5)
    password_entry.pack(side=RIGHT, padx=5, pady=5)
    login_button.pack(anchor="center")

    # signInlabel.grid(column=0, row=0, columnspan=2, pady=10)
    # user_label.grid(column=0, row=1, sticky="W", padx=5, pady=5)
    # user_entry.grid(column=1, row=1, sticky="W", padx=5, pady=5)
    # password_label.grid(column=0, row=2, sticky="W", padx=5, pady=5)
    # password_entry.grid(column=1, row=2, sticky="W", padx=5, pady=5)
    # login_button.grid(column=1, row=3, sticky="W", padx=5, pady=5)


def main_page():
    # MAKING WIDGETS
    frame = Frame(root_window, bg="#DACEC4")
    frame.tkraise()
    logout = Button(
        frame, text="Log Out", command=lambda: [clear_screen(frame), login()]
    )
    mainPglabel = Label(frame, text="Welcome to Task Manager", font=("", 24))
    task_entry = Entry(frame)
    description_entry = Entry(frame)
    submit_button = Button(
        frame,
        text="Submit",
        command=lambda: [
            add_task(task_entry.get(), description_entry.get(), theList),
            clear_fields(task_entry, description_entry),
        ],
    )
    theList = Listbox(
        frame, width=35, height=10, bg="SystemButtonFace", bd=0, fg="#464646"
    )

    # CALLING WIDGETS
    logout.pack()
    frame.pack(anchor="center", padx=10, pady=10)
    mainPglabel.pack(side="top", pady=10)
    theList.pack()
    task_entry.pack(pady=10)
    description_entry.pack(pady=5, padx=5)
    submit_button.pack(padx=5, pady=5)
    query_tasks(theList)


login()

# query_tasks()

root_window.mainloop()

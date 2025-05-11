from tkinter import END
import sqlite3
from . import misc, task_screen, main_page


def query_tasks(theList, user):
    dataConnector = sqlite3.connect("toDo.db")
    cursor = dataConnector.cursor()
    userID = user[0]

    if user[3] == 1:
        cursor.execute("SELECT * FROM tasks")
    else:
        cursor.execute(
            """SELECT *
        FROM tasks
        WHERE tID IN
        (
        SELECT tID FROM UserTasks WHERE uID = ?
        )""",
            [userID],
        )
    tasklist = cursor.fetchall()

    theList.delete(0, END)

    for task in tasklist:
        theList.insert(END, f"{task[0]}: {task[1]}")

    dataConnector.close()


def add_task(task, description, status, due_date, involved, theList, user):
    """Insert a new task into the database and refresh the task list."""
    if task.strip() == "":  # Prevent empty tasks
        return

    users = involved.split(",")
    dataConnector = sqlite3.connect("toDo.db")
    cursor = dataConnector.cursor()

    try:
        # Later, put actual involved people
        cursor.execute(
            "INSERT INTO Tasks (task_name, description, status, due_date, involved) VALUES (?, ?, ?, ?, ?)",
            [task, description, status, due_date, involved],
        )
        taskID = cursor.lastrowid
        for uID in users:
            cursor.execute(
                "INSERT INTO UserTasks (uID,tID) VALUES (?,?)", [uID, taskID]
            )
        dataConnector.commit()

    except sqlite3.IntegrityError:
        print("Task already exists!")  # Avoid duplicate tasks

    dataConnector.close()
    query_tasks(theList, user)


def delete_task(theList, user):
    try:
        selected = theList.get(theList.curselection())
        tID = int(selected.split(":")[0])  # Get tID from "tID: task name"

        dataConnector = sqlite3.connect("toDo.db")
        cursor = dataConnector.cursor()
        cursor.execute("PRAGMA foreign_keys=ON")

        cursor.execute("DELETE FROM Tasks WHERE tID = ?", [tID])
        dataConnector.commit()
        dataConnector.close()

        query_tasks(theList, user)

    except:
        misc.pop_up("Invalid task selected")


# returns the task that is selected by mouse from the given list #
def selected_item(theList, user):
    try:
        selected = theList.get(theList.curselection())
        tID = int(selected.split(":")[0])  # Get tID from "tID: task name"
        dataConnector = sqlite3.connect("toDo.db")
        cursor = dataConnector.cursor()

        cursor.execute("SELECT * FROM Tasks WHERE tID = ?", [tID])
        task = cursor.fetchone()

        task_screen.task_screen(task, user)

        dataConnector.close()
    except:
        if user[3] == 1:
            main_page.admin_page(user)
        else:
            main_page.main_page(user)
        misc.pop_up("Invalid task selected")

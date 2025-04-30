from tkinter import END
import sqlite3
from . import misc, task_screen, main_page


def query_tasks(theList):
    dataConnector = sqlite3.connect("toDo.db")
    cursor = dataConnector.cursor()

    cursor.execute("SELECT * FROM tasks")
    tasklist = cursor.fetchall()

    theList.delete(0, END)

    for task in tasklist:
        theList.insert(END, f"{task[0]}: {task[1]}")

    dataConnector.close()


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


def delete_task(theList):
    try:
        selected = theList.get(theList.curselection())
        tID = int(selected.split(":")[0])  # Get tID from "tID: task name"

        dataConnector = sqlite3.connect("toDo.db")
        cursor = dataConnector.cursor()

        cursor.execute("DELETE FROM Tasks WHERE tID = ?", (tID,))
        dataConnector.commit()
        dataConnector.close()

        query_tasks(theList)

    except:
        misc.pop_up("Invalid task selected")


# returns the task that is selected by mouse from the given list #
def selected_item(theList):
    try:
        selected = theList.get(theList.curselection())
        tID = int(selected.split(":")[0])  # Get tID from "tID: task name"
        dataConnector = sqlite3.connect("toDo.db")
        cursor = dataConnector.cursor()

        cursor.execute("SELECT * FROM tasks WHERE tID = ?", [tID])
        task = cursor.fetchone()

        task_screen.task_screen(task)

        dataConnector.close()
    except:
        main_page.main_page()
        misc.pop_up("Invalid task selected")

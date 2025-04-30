import sqlite3
from functions import login, root_window


### SETTING UP DATABASE ###
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


# we only call login screen because
# it is the first screen the user will see.
login.login()

root_window.root_window.mainloop()

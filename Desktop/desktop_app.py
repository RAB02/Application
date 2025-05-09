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
    cursor.execute("""CREATE TABLE SignIn (
        sID         integer,
        username    text NOT NULL,
        password    text NOT NULL,
        PRIMARY KEY(sID AUTOINCREMENT)
    )""")

listOfTables = cursor.execute(
    "SELECT name FROM sqlite_master WHERE type='table' AND name='Users'"
).fetchall()
if listOfTables == []:
    cursor.execute("""CREATE TABLE Users (
	uID         integer NOT NULL,
        first_name  text,
        last_name   text,
        admin       integer DEFAULT 0,
        PRIMARY KEY(uID AUTOINCREMENT)
    )""")

listOfTables = cursor.execute(
    "SELECT name FROM sqlite_master WHERE type='table' AND name='Tasks'"
).fetchall()
if listOfTables == []:
    cursor.execute("""CREATE TABLE Tasks (
        tID         integer,
        task_name   text,
        description text,
        status      text,
        due_date    text,
        involved    integer,
        PRIMARY KEY(tID AUTOINCREMENT),
        FOREIGN KEY(involved) REFERENCES Users(uID)
    )""")

listOfTables = cursor.execute(
    "SELECT name FROM sqlite_master WHERE type='table' AND name='Login_to_User'"
).fetchall()
if listOfTables == []:
    cursor.execute("""CREATE TABLE Login_to_User (
    sID	    INTEGER,
	uID	    INTEGER,
	PRIMARY KEY(sID,uID),
	FOREIGN KEY(sID) REFERENCES "SignIn"("sID") ON DELETE CASCADE,
	FOREIGN KEY(uID) REFERENCES "Users"("uID") ON DELETE CASCADE
    )""")

dataConnector.commit()
dataConnector.close()


# we only call login screen because
# it is the first screen the user will see.
login.login()

root_window.root_window.mainloop()

from tkinter import Frame, Label, Entry, Button, LEFT, RIGHT
from . import misc, main_page, root_window
import sqlite3


def check_login(username, password, frame):
    dataConnector = sqlite3.connect("toDo.db")
    cursor = dataConnector.cursor()

    cursor.execute(
        "SELECT * FROM SignIn WHERE username = ? AND password = ?", [username, password]
    )
    if cursor.fetchall():
        misc.clear_screen(frame)
        main_page.main_page()

    else:
        misc.pop_up("INVALID LOG IN")
    return


def login():
    # MAKING WIDGETS
    login_frame = Frame(root_window.root_window, bg="#DACEC4")
    user_frame = Frame(login_frame, bg="#DACEC4")
    signInlabel = Label(login_frame, text="Log In", bg="#DACEC4", font=("", 24))
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
    to_signup_button = Button(
        login_frame,
        text="Sign-up",
        command=lambda: [misc.clear_screen(login_frame), signup()],
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
    to_signup_button.pack(anchor="center")


def check_signup(username, password, frame):
    if len(password) < 4:
        misc.pop_up("Password must be more 4 or more characters")
    else:
        dataConnector = sqlite3.connect("toDo.db")
        cursor = dataConnector.cursor()

        cursor.execute(
            "INSERT INTO SignIn (username, password) VALUES (?,?)", [username, password]
        )
        dataConnector.commit()
        misc.clear_screen(frame)
        login()
        return


def signup():
    signup_frame = Frame(root_window.root_window, bg="#DACEC4")

    user_frame = Frame(signup_frame, bg="#DACEC4")
    signInlabel = Label(signup_frame, text="Sign Up", bg="#DACEC4", font=("", 24))
    user_label = Label(user_frame, text="Username: ", bg="#DACEC4")
    user_entry = Entry(user_frame)
    password_frame = Frame(signup_frame, bg="#DACEC4")
    password_label = Label(password_frame, text="Password: ", bg="#DACEC4")
    password_entry = Entry(password_frame, show="*")
    signup_button = Button(
        signup_frame,
        text="Sign Up",
        command=lambda: check_signup(
            user_entry.get(), password_entry.get(), signup_frame
        ),
    )
    to_login_button = Button(
        signup_frame,
        text="Login",
        command=lambda: [misc.clear_screen(signup_frame), login()],
    )

    # CALLING WIDGETS
    signup_frame.pack(anchor="center", pady=10, expand=True)
    signInlabel.pack(pady=10)
    user_frame.pack()
    password_frame.pack()
    user_label.pack(side=LEFT, padx=5, pady=5)
    user_entry.pack(side=RIGHT, padx=5, pady=5)
    password_label.pack(side=LEFT, padx=5, pady=5)
    password_entry.pack(side=RIGHT, padx=5, pady=5)
    signup_button.pack(anchor="center")
    to_login_button.pack(anchor="center")

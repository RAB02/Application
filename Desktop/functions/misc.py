import tkinter.messagebox
from tkinter import END


# Clears the screen so that we can show another frame
def clear_screen(frame):
    frame.pack_forget()
    return


# Makes pop-up window
def pop_up(error):
    tkinter.messagebox.showinfo("ERROR", error)


# Clears the fields from the input
def clear_fields(task, description, status, due_date, involved):
    task.delete(0, END)
    description.delete(0, END)
    status.delete(0, END)
    due_date.delete(0, END)
    involved.delete(0, END)

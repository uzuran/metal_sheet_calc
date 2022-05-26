from tkinter import *
from tkinter import ttk
import hashlib
import os


# Add main screen basic function with the parameters.
def main_screen():
    """This is the basic main_screen, with some parameters, labels, colors, buttons and screen main.loop()
    function"""
    global screen
    screen = Tk()
    screen.geometry("350x200")
    screen.title("Metal sheet calculator.")
    screen.eval('tk::PlaceWindow . center')

    # Main label.
    Label(text="Please login!Or register.", bg="#d1dffa", width="300", height="2",
          font=("Calibri", 13)).pack()

    # Blank line.
    Label(text="").pack()

    # Login button.
    Button(text="Login", width="30", height="2", command=login).pack()

    # Blank line.
    Label(text="").pack()

    # Register button.
    Button(text="Register", width="30", height="2", command=register).pack()

    screen.mainloop()


# Add a new window for register users.
def register():
    """This was the second screen for register new users"""
    global second_screen
    """Add a new screen parameters at top of level main screen"""
    second_screen = Toplevel(screen)
    second_screen.geometry("350x450")
    second_screen.title("Metal sheet calculator.")

    # Global
    global user_name
    global password
    global user_name_entry
    global pass_entry

    # Add username, password string line.
    user_name = StringVar()
    password = StringVar()

    # Main label.
    Label(second_screen, text="Please enter your name and password.", bg="#d1dffa", width="300", height="2",
          font=("Calibri", 13)).pack()

    # Blank line.
    Label(second_screen, text="").pack()

    # Username label.
    Label(second_screen, text="Username").pack()

    # User entry.
    user_name_entry = Entry(second_screen, textvariable=user_name)
    user_name_entry.pack()

    # Blank line.
    Label(second_screen, text="").pack()
    # Password label.
    Label(second_screen, text="Password").pack()

    # User password entry.
    pass_entry = Entry(second_screen, textvariable=password, show="*")
    pass_entry.pack()

    # Blank line.
    Label(second_screen, text="").pack()
    # Register button.
    Button(second_screen, text="Register", width=10, height=1, command=register_users).pack()


# Register user and add all information inside text document.
def register_users():
    """Function for register new users, validate name without numbers,store all info in text file, hash password."""
    username_info = user_name.get()
    password_info = password.get()

    # If username have some numbers label send it on screen.
    if username_info.isdigit():
        Label(second_screen, text="You can not have a numbers in name! ", fg="red",
              font=("Calibri", 11)).pack()

    # If password have only blank on field label say it.
    elif password_info == "":
        Label(second_screen, text="Password can not contain the blank line", fg="red",
              font=("Calibri", 11)).pack()
    else:
        hashed = hashlib.md5(str.encode(password_info)).hexdigest()
        # Open file with the write mode, write the info of the name and hashed password
        file = open(username_info, "w")
        file.write(username_info + "\n")
        hashed_to_str = str(hashed)
        file.write(hashed_to_str)
        file.close()

        user_name_entry.delete(0, END)
        pass_entry.delete(0, END)

        Label(second_screen, text='Registration success.', fg="green", font=("Calibri", 11)).pack()


def login():
    """This was login screen"""
    global third_screen
    third_screen = Toplevel(screen)
    third_screen.title("Please login !")
    third_screen.geometry("350x450")

    # Main label.
    Label(third_screen, text="Please login!", bg="#d1dffa", width="300", height="2",
          font=("Calibri", 13)).pack()
    # Blank line.
    Label(text="").pack()

    global user_name_verify
    global user_pass_verify
    global user_name_entry1
    global user_pass_entry2

    user_name_verify = StringVar()
    user_pass_verify = StringVar()

    # Username label
    Label(third_screen, text="Username").pack()

    # Username entry.
    user_name_entry1 = Entry(third_screen, textvariable=user_name_verify)
    user_name_entry1.pack()

    # Blank line.
    Label(third_screen, text="").pack()
    Label(third_screen, text="Password").pack()

    # User pass entry.
    user_pass_entry2 = Entry(third_screen, textvariable=user_pass_verify, show="*")
    user_pass_entry2.pack()

    # Blank line.
    Label(third_screen, text="").pack()

    # Login button.
    Button(third_screen, text="Login", width=10, height=1, command=login_verify).pack()


def login_verify():
    user_name_v = user_name_verify.get()
    password_v = user_pass_verify.get()

    user_name_entry1.delete(0, END)
    user_pass_entry2.delete(0, END)

    list_of_users = os.listdir()

    password_v = hashlib.md5(str.encode(password_v)).hexdigest()

    if user_name_v in list_of_users:
        file1 = open(user_name_v, "r")
        verify = file1.read().splitlines()

        if password_v in verify:
            Label(third_screen, text="Login success!", fg="green",
                  font=("Calibri", 11)).pack()

            # Add a forth main screen for calculate sheet material.
            forth_screen = Toplevel(third_screen)

            # getting screen width and height of display
            width = forth_screen.winfo_screenwidth()
            height = forth_screen.winfo_screenheight()
            # setting tkinter window size
            forth_screen.geometry("%dx%d" % (width, height))
            forth_screen.title("Metal sheet calculator.")

            Label(forth_screen, text="Metal sheet calculator.", bg="#d1dffa", width="300", height="2",
                  font=("Calibri", 13)).pack()

            notebook = ttk.Notebook(forth_screen)
            notebook.pack(anchor='center')

            my_frame1 = Frame(notebook, width=500, height=500)
            my_frame2 = Frame(notebook, width=500, height=500)
            my_frame3 = Frame(notebook, width=500, height=500)

            steel_label = Label(my_frame1, text="Steel material")
            steel_id = Label(my_frame1, text="id:")

            al_label = Label(my_frame2, text="Al material")
            spec_label = Label(my_frame3, text="Special")

            steel_label.pack(padx=5, pady=5)
            al_label.pack(padx=5, pady=5)
            spec_label.pack(padx=5, pady=5)
            steel_id.pack(anchor="w")

            my_frame1.pack(padx=5, pady=5)
            my_frame2.pack(padx=5, pady=5)

            notebook.add(my_frame1, text="Steel material")
            notebook.add(my_frame2, text="Aluminium material")
            notebook.add(my_frame3, text="Special material")


        else:
            Label(third_screen, text="Password was wrong!", fg="red",
                  font=("Calibri", 11)).pack()
    else:
        Label(third_screen, text="User not found !", fg="red",
              font=("Calibri", 11)).pack()




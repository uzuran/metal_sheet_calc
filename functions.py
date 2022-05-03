from tkinter import *
import bcrypt


# Add main screen basic function with the parameters.
def main_screen():
    """This is the basic main_screen, with some parameters, labels, colors, buttons and screen main.loop() function"""
    global screen
    screen = Tk()
    screen.geometry("350x200")
    screen.title("Metal sheet calculator.")
    Label(text="Please login!Or register.", bg="#d1dffa", width="300", height="2", font=("Calibri", 13)).pack()

    # Blank line.
    Label(text="").pack()
    Button(text="Login", width="30", height="2", command=login).pack()
    # Blank line.
    Label(text="").pack()
    Button(text="Register", width="30", height="2", command=register).pack()

    screen.mainloop()


def login():
    """This was login screen"""
    global third_screen
    third_screen = Toplevel(screen)
    third_screen.title("Please login !")
    third_screen.geometry("350x450")
    Label(third_screen, text="Please login!", bg="#d1dffa", width="300", height="2", font=("Calibri", 13)).pack()
    # Blank line.
    Label(text="").pack()

    global user_name_verify
    global user_pass_verify

    user_name_verify = StringVar()
    user_pass_verify = StringVar()
    Label(third_screen, text="Username").pack()
    user_name_entry1 = Entry(third_screen, textvariable=user_name_verify)
    user_name_entry1.pack()
    Label(third_screen, text="").pack()
    Label(third_screen, text="Password").pack()
    user_pass_entry2 = Entry(third_screen, textvariable=user_pass_verify)
    user_pass_entry2.pack()
    Label(third_screen, text="").pack()
    Button(third_screen, text="Login", width=10, height=1).pack()


# Add a new window for register users.
def register():
    """This was the second screen for register new users"""
    global second_screen
    """Add a new screen parameters at top of level main screen"""
    second_screen = Toplevel(screen)
    second_screen.geometry("350x450")
    second_screen.title("Metal sheet calculator.")

    global user_name
    global password
    global user_name_entry
    global pass_entry

    # Add username, password string line.
    user_name = StringVar()
    password = StringVar()

    Label(second_screen, text="Please enter your name and password.", bg="#d1dffa", width="300", height="2",
          font=("Calibri", 13)).pack()
    Label(second_screen, text="").pack()
    Label(second_screen, text="Username").pack()
    user_name_entry = Entry(second_screen, textvariable=user_name)
    user_name_entry.pack()
    # Blank line.
    Label(second_screen, text="").pack()
    Label(second_screen, text="Password").pack()
    pass_entry = Entry(second_screen, textvariable=password, show="*")
    pass_entry.pack()
    Label(second_screen, text="").pack()
    Button(second_screen, text="Register", width=10, height=1, command=register_users).pack()


# Register user and add all information inside text document.
def register_users():
    """Function for register new users, validate name without numbers,store all info in text file, hash password."""
    username_info = user_name.get()
    password_info = password.get()

    if username_info.isalnum():
        Label(second_screen, text="You can not have a numbers in name! ", fg="red",
              font=("Calibri", 11)).pack()

    elif password_info == "":
        Label(second_screen, text="Password can not contain the blank line", fg="red",
              font=("Calibri", 11)).pack()
    else:
        # From str to bytes.
        byte_pass = bytes(password_info, encoding='utf8')
        # Generate salt.
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(byte_pass, salt)
        # Open file with the write mode, write the info of the name and hashed password
        file = open(username_info, "w")
        file.write(username_info + "\n")
        hashed_to_str = str(hashed)
        file.write(hashed_to_str)
        file.close()

        user_name_entry.delete(0, END)
        pass_entry.delete(0, END)

        Label(second_screen, text='Registration success.', fg="green", font=("Calibri", 11)).pack()

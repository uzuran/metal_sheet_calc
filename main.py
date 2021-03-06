import tkinter as tk
from main_work_screen import main_work_space
from admin_screen import admin_screen_window
from tkinter import *
from tkinter import ttk
import hashlib
import os
import os.path
from os import path


class MainFrame(ttk.Frame):
    """This is the basic MainFrame(app)"""
    def __init__(self, container):
        super().__init__(container, )

        options = {"padx": 5, "pady": 5}
        enter_label_options = {"text": "Please login, or register.",
                                "bg": "#d1dffa",
                                "width": "300",
                                "height": "2",
                                "font": "Calibri, 12"}

        # Enter label.
        self.enter_label = Label(self, **enter_label_options)
        self.enter_label.pack(**options)

        # Options for buttons.
        btn_options_l = {"text": "Log in",
                         "width": "30",
                         "height": "2"
                         }

        # Log in button.
        self.log_in_button = Button(self, **btn_options_l)
        # Command for button
        self.log_in_button['command'] = self.login
        self.log_in_button.pack(**options)

        btn_options_r = {"text": "Register",
                         "width": "30",
                         "height": "2"

                         }

        # Register button.
        self.register_button = Button(self, **btn_options_r)
        # Command for button
        self.register_button['command'] = self.register_click
        self.register_button.pack(**options)

        # show the frame on the container
        self.pack()

        # Function for open new window with registration.
    def register_click(self):
        self.register_window = Toplevel(frame)
        self.register_window.geometry("350x450")
        self.register_window.title("Steel sheet calculator.")

        # Global
        global user_name
        global password
        global user_name_entry
        global pass_entry

        # Add username, password string line.
        user_name = StringVar()
        password = StringVar()

        # Register options.
        register_label_option = {
            "text": "Please enter your name and password.",
            "bg": "#d1dffa",
            "width": "300",
            "height": "2",
            "font": "Calibri, 12"
        }


        # Register window label.
        register_label = Label(self.register_window, **register_label_option)
        register_label.pack()

        # User name label.
        user_n = Label(self.register_window, text="Username")
        user_n.pack()

        # Username entry.
        user_name_entry = Entry(self.register_window, textvariable=user_name)
        user_name_entry.pack()

        # Password label.
        pass_label = Label(self.register_window, text="Password")
        pass_label.pack()

        # User password entry.
        pass_entry = Entry(self.register_window, textvariable=password, show="*")
        pass_entry.pack()

        register_btn_option = {
            "text": "Register",
            "width": "10",
            "height": "1"
        }

        # Register button.
        register_user_button = Button(self.register_window, **register_btn_option)
        # Command for button
        register_user_button['command'] = self.register_users
        register_user_button.pack()
        # Bind Enter key for entry lines.
        user_name_entry.bind("<Return>", self.register_users)
        pass_entry.bind("<Return>", self.register_users)

    # Register user and add all information inside text document.
    def register_users(self, event=None):
        """Function for register new users, validate name without numbers,store all info in text file, hash password."""
        username_info = user_name.get()
        password_info = password.get()
        list_of_users = os.listdir()
        # If username have some numbers label send it on screen.
        options = {"text": "You can not have a numbers, or blank line in name!",
                   "fg": "red",
                   "font": "Calibri, 12"}

        if username_info.isdigit():
            no_num = Label(self.register_window, **options)
            no_num.pack()
            # If password have only blank on field label say it.

        elif password_info == "":
            pass_inf = Label(self.register_window, **options)
            pass_inf.pack()

        elif username_info in list_of_users:
            user_ex = Label(self.register_window, text="User exist", fg="red")
            user_ex.pack()

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

            # Label option
            success_option = {"text": "Registration success.",
                              "fg": "green",
                              "font": "Calibri, 11"}

            reg_success = Label(self.register_window, success_option)
            reg_success.pack()

    def login(self):
        """This was login screen"""
        self.login_screen = Toplevel(frame)
        self.login_screen.title("Please login!")
        self.login_screen.geometry("350x450")

        login_l_option = {"text": "Please login, or register",
                          "bg": "#d1dffa",
                          "width": "300",
                          "height": "2",
                          "font": "Calibri, 13"}
        # Main label.
        login_label = Label(self.login_screen, ** login_l_option)
        login_label.pack()

        global user_name_verify
        global user_pass_verify
        global user_name_entry1
        global user_pass_entry2

        user_name_verify = StringVar()
        user_pass_verify = StringVar()

        # Username label
        Label(self.login_screen, text="Username").pack()

        # Username entry.
        user_name_entry1 = Entry(self.login_screen, textvariable=user_name_verify)
        user_name_entry1.pack()

        # Blank line.
        Label(self.login_screen, text="").pack()
        Label(self.login_screen, text="Password").pack()

        # User pass entry.
        user_pass_entry2 = Entry(self.login_screen, textvariable=user_pass_verify, show="*")
        user_pass_entry2.pack()

        # Login button option.
        login_btn_option = {"text": "Login",
                            "width": "10",
                            "height": "1",
                            }
        # Login button.
        login_user_button = Button(self.login_screen, **login_btn_option)
        # Command for button
        login_user_button['command'] = self.login_verify
        # user_pass_entry bind for enter use.
        user_pass_entry2.bind("<Return>", self.login_verify)
        user_name_entry1.bind("<Return>", self.login_verify)
        login_user_button.pack()

    # Login verify function for check users.
    def login_verify(self, event=None):
        user_name_v = user_name_verify.get()
        password_v = user_pass_verify.get()
        # Clean entry after press the button.
        user_name_entry1.delete(0, END)
        user_pass_entry2.delete(0, END)

        list_of_users = os.listdir()

        # Hash password.
        password_v = hashlib.md5(str.encode(password_v)).hexdigest()

        # If user are in directory read lines and verify.
        if user_name_v == "admin":
            activator = True
            if path.exists(user_name_v) == activator:

                file1 = open(user_name_v, "r")
                verify = file1.read().splitlines()

                if password_v in verify:

                    pass_success_option = {"text": "Login success",
                                       "fg": "green",
                                       "font": "Calibri, 12"}

                    pass_success = Label(self.login_screen, ** pass_success_option)
                    pass_success.pack()

                    # Add next file with the func main screen,space for better reading code, main_work_screen.py.

                    admin_screen_window(user_name_v)
                elif user_name_v == "admin":
                    Label(self.login_screen, text='You need a password!', fg='red').pack()
            else:
                Label(self.login_screen, text='Admin not exist!', fg='red').pack()

        elif user_name_v in list_of_users:
            file1 = open(user_name_v, "r")
            verify = file1.read().splitlines()

            if password_v in verify:
                pass_success_option = {"text": "Login success",
                                        "fg": "green",
                                        "font": "Calibri, 12"}

                pass_success = Label(self.login_screen, **pass_success_option)
                pass_success.pack()

                # Add next file with the func main screen,space for better reading code, main_work_screen.py.
                main_work_space(user_name_v)

            else:
                Label(self.login_screen, text="Password was wrong!", fg="red", font=("Calibri", 11)).pack()
        else:
            Label(self.login_screen, text="User not found !", fg="red", font=("Calibri", 11)).pack()


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        # configure the root window
        self.title("Steel sheet calculator.")
        self.geometry("350x200")
        self.eval("tk::PlaceWindow . center")
        #self.iconbitmap('./assets/pythontutorial.ico')


if __name__ == "__main__":
    app = App()
    frame = MainFrame(app)
    app.mainloop()



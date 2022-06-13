from tkinter import *
from tkinter import ttk
from st1_admin import st1_admin_line


def admin_screen(user_name_v):
    admin_screen = Toplevel()
    admin_screen.title("Steel sheet calculator.")

    # setting tkinter window size
    admin_screen.geometry("%dx%d" % (1000, 600))
    admin_screen.title("Steel sheet calculator.")

    # Main label.
    label_option = {"text": "Steel sheet calculator",
                    "bg": "#d1dffa",
                    "width": "300",
                    "height": "2",
                    "font": "Calibri, 13"}

    main_label = Label(admin_screen, ** label_option)
    main_label.pack()

    # Check users,  who is log in.
    user_name_label = user_name_v

    check_user = Label(admin_screen, text=str(user_name_label) + " Is log in now.", bg="green")
    check_user.pack(anchor="w")

    # Add notebok of a materials.
    notebook = ttk.Notebook(admin_screen)
    notebook.pack(anchor='center')

    # Add frame options.
    frame_options = {"width": "500",
                     "height": "500"}

    my_frame1 = Frame(notebook, ** frame_options)
    my_frame2 = Frame(notebook, ** frame_options)
    my_frame3 = Frame(notebook, ** frame_options)
    my_frame4 = Frame(notebook, **frame_options)

    # Add notebook on screen.
    notebook.add(my_frame1, text="Steel material")
    notebook.add(my_frame2, text="Aluminium material")
    notebook.add(my_frame3, text="Stainless steel material")
    notebook.add(my_frame4, text="Special material")

    st1_admin_line(my_frame1)


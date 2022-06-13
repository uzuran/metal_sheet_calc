from tkinter import *
from tkinter import ttk
import pickle
from tkinter import messagebox as msg
from st1_user import st1_user_line

def main_work_space(user_name_v):
    main_work_screen = Toplevel()
    main_work_screen.title("Metal sheet calculator.")

    # getting screen width and height of display
    width = main_work_screen.winfo_screenwidth()
    height = main_work_screen.winfo_screenheight()
    # setting tkinter window size
    main_work_screen.geometry("%dx%d" % (width, height))
    main_work_screen.title("Steel sheet calculator.")

    # Main label.
    label_option = {"text": "Steel sheet calculator",
                    "bg": "#d1dffa",
                    "width": "300",
                    "height": "2",
                    "font": "Calibri, 13"}

    main_label = Label(main_work_screen, ** label_option)
    main_label.pack()

    # Check users,  who is log in.
    user_name_label = user_name_v

    check_user = Label(main_work_screen, text=str(user_name_label) + " Is log in now..", bg="green")
    check_user.pack(anchor="w")

    # Add notebook of a materials.
    notebook = ttk.Notebook(main_work_screen)
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

    # Add first line st1 steel material
    st1_user_line(my_frame1, main_work_screen)




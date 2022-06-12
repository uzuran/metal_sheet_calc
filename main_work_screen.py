import tkinter
from tkinter import *
from tkinter import ttk
import pickle
from tkinter import messagebox as msg
from st_1 import st1_line

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

    # Steel id
    steel_id = Label(my_frame1, text="ID:", )
    steel_id.grid(row=0)

    # Steel id
    steel_id = Label(my_frame1, text="ID:", )
    steel_id.grid(row=0)
    steel_id = Label(my_frame1, text="0116000")
    steel_id.grid(row=1)
    # Steel thickness
    steel_thickness = Label(my_frame1, text="Thickness:", )
    steel_thickness.grid(column=1, row=0)
    steel_thickness = Label(my_frame1, text="1")
    steel_thickness.grid(column=1, row=1)

    # Steel X> mm

    steel_x = Label(my_frame1, text="X>:", )
    steel_x.grid(column=2, row=0)
    steel_x = Label(my_frame1, text="2000")
    steel_x.grid(column=2, row=1)

    # Steel Y^ mm

    steel_y = Label(my_frame1, text="Y^:", )
    steel_y.grid(column=3, row=0)
    steel_y = Label(my_frame1, text="1000")
    steel_y.grid(column=3, row=1)

    # Ordered material.
    steel_ordered = Label(my_frame1, text="Ordered material:")
    steel_ordered.grid(column=5, row=0)

    load_pickle = open("st1.pickle", "rb")
    load_order = pickle.load(load_pickle)

    ordered_value = Label(my_frame1, text=load_order)
    ordered_value.grid(column=5, row=1)

    def update():
        ordered_value.after(1, update)
        ordered_value.configure(text=str(load_order))
    update()



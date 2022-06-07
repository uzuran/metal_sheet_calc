from tkinter import *
from tkinter import ttk
import pickle


def admin_screen(user_name_v, ):
    admin_screen = Toplevel()
    admin_screen.title("Metal sheet calculator.")

    # getting screen width and height of display
    width = admin_screen.winfo_screenwidth()
    height = admin_screen.winfo_screenheight()
    # setting tkinter window size
    admin_screen.geometry("%dx%d" % (width, height))
    admin_screen.title("Metal sheet calculator.")

    # Main label.
    label_option = {"text": "Metal sheet calculator",
                    "bg": "#d1dffa",
                    "width": "300",
                    "height": "2",
                    "font": "Calibri, 13"}

    main_label = Label(admin_screen, ** label_option)
    main_label.pack()

    # Check users,  who is log in.
    user_name_label = user_name_v

    check_user = Label(admin_screen, text=str(user_name_label) + " Is online now.", bg="green")
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

    # Add notebook on screen.
    notebook.add(my_frame1, text="Steel material")
    notebook.add(my_frame2, text="Aluminium material")
    notebook.add(my_frame3, text="Special material")

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

    # Button minus.

    steel_minus = Label(my_frame1, text="btn - ")
    steel_minus.grid(column=4, row=0)
    steel_button = Button(my_frame1, text="-")
    steel_button.grid(column=4, row=1)

    # Ordered material.
    steel_ordered = Label(my_frame1, text="Ordered material:")
    steel_ordered.grid(column=5, row=0)

    def get_from_var():
        print(variable.get())

    def add_to_data_text():
        with open("st1.pickle", "wb") as f:
            var_get = variable.get()
            pickle.dump(var_get, f)
            ordered_value.configure(text=var_get)
            f.close()

    order_open = open("st1.pickle", "rb")
    ordered = pickle.load(order_open)

    try:
        if ordered == "":
            ordered = {}
    except EOFError:
        print("File empty ")

    ordered_value = Label(my_frame1, text=str(ordered))
    ordered_value.grid(column=5, row=1, sticky=W)

    def plus():
        a_file = open("St_1_order", "w+")
        file_data = a_file.read()
        variable_g = variable.get()

        for line in a_file:
            line_list = line.split()
            for i in range(len(line_list)):
                value_p = int(line_list[i]) + variable_g

                replace = file_data.replace(value_p, a_file)
                a_file.write(replace)

        a_file.close()

    # Spinbox
    variable = IntVar()
    spin_box = ttk.Spinbox(
        my_frame1,
        textvariable=variable,
        from_=0,
        to=200,
        width=5,
        command=get_from_var
    )
    spin_box.grid(column=5, row=1, sticky=E)

    # Label add material.
    steel_plus = Label(my_frame1, text="add material")
    steel_plus.grid(column=6, row=0)

    # Add material button.
    add_material_button = Button(my_frame1, text='add', width=5)
    # Command for button
    add_material_button['command'] = add_to_data_text
    add_material_button.grid(column=6, row=1)

    # Button plus
    steel_plus = Label(my_frame1, text="btn")
    steel_plus.grid(column=7, row=0)
    steel_button = Button(my_frame1, text="+", command=plus)
    steel_button.grid(column=7, row=1)
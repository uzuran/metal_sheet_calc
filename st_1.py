from tkinter import *
from tkinter import ttk
import pickle
from tkinter import messagebox as msg


def st1_line(my_frame1):
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

        def minus():
            answer = msg.askyesno("Write off material",
                                  f"Are you sure that you want write off this {variable.get()} count of material?")
            activator = True
            if answer == activator:

                try:
                    order_pickle = open("st1.pickle", "rb")
                    from_pickle = pickle.load(order_pickle)
                    total = from_pickle - variable.get()

                    with open("st1.pickle", "wb") as w:
                        pickle.dump(total, w)
                        ordered_value.configure(text=total)

                except Exception as ex:
                    print("Error during unpickling object (Possibly unsupported):", ex)
            else:
                msg.showinfo(title="Write off canceling", message="Write off canceling you can back to work.")
        # Button minus.
        steel_minus = Label(my_frame1, text="btn - ")
        steel_minus.grid(column=4, row=0)
        steel_decrease_button = Button(my_frame1, text="-")
        steel_decrease_button['command'] = minus
        steel_decrease_button.grid(column=4, row=1)

        # Ordered material.
        steel_ordered = Label(my_frame1, text="Ordered material:")
        steel_ordered.grid(column=5, row=0)

        # Add numbers of ordered material at pickle datastorage.
        def add_to_order_pickle():
            try:
                with open("st1.pickle", "wb") as f:
                    pickle.dump(variable.get(), f)
                    ordered_value.configure(text=variable.get())
            except Exception as ex:
                print("Error during pickling object (Possibly unsupported):", ex)

        load_pickle = open("st1.pickle", "rb")
        load_order = pickle.load(load_pickle)

        ordered_value = Label(my_frame1, text=load_order)
        ordered_value.grid(column=5, row=1, sticky=W)

        # Add plus function, for addition material at order.
        def plus():
            try:
                order_pickle = open("st1.pickle", "rb")
                from_pickle = pickle.load(order_pickle)
                total = from_pickle + variable.get()

                with open("st1.pickle", "wb") as w:
                    pickle.dump(total, w)
                    ordered_value.configure(text=total)

            except Exception as ex:
                print("Error during unpickling object (Possibly unsupported):", ex)

        # Spinbox
        variable = IntVar()
        spin_box = ttk.Spinbox(
            my_frame1,
            textvariable=variable,
            from_=0,
            to=200,
            width=5,
        )
        spin_box.grid(column=5, row=1, sticky=E)

        # Label add material.
        steel_plus = Label(my_frame1, text="Add material:")
        steel_plus.grid(column=6, row=0)

        # Add material button.
        add_material_button = Button(my_frame1, text='add', width=5)
        # Command for button
        add_material_button['command'] = add_to_order_pickle
        add_material_button.grid(column=6, row=1)

        # Button plus
        steel_plus = Label(my_frame1, text="btn")
        steel_plus.grid(column=7, row=0)
        steel_addition_button = Button(my_frame1, text="+")
        steel_addition_button['command'] = plus
        steel_addition_button.grid(column=7, row=1)

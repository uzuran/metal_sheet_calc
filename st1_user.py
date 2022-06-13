from tkinter import *
from tkinter import ttk
import pickle
from tkinter import messagebox as msg


def st1_user_line(my_frame1, main_work_screen):
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

    # Function for update order label.
    def update_order():
        load_pickle = open("st1.pickle", "rb")
        load_order = pickle.load(load_pickle)

        ordered_value = Label(my_frame1)
        ordered_value.grid(column=5, row=1)
        ordered_value['text'] = load_order
        main_work_screen.after(1000, update_order)

    update_order()

    def update_storage():
        load_pickle = open("st1_storage.pickle", "rb")
        material_in = pickle.load(load_pickle)

        material_in_storage = Label(my_frame1, text=material_in)
        material_in_storage['text'] = material_in
        material_in_storage.grid(column=6, row=1, sticky=W)
        main_work_screen.after(1000, update_storage)

    update_storage()

    # Label Material in storage.
    material_in_label = Label(my_frame1, text="Material in storage:")
    material_in_label.grid(column=6, row=0)

    # Spinbox order.
    material_in_str = IntVar()
    spin_box = ttk.Spinbox(
        my_frame1,
        textvariable=material_in_str,
        from_=0,
        to=200,
        width=5,
    )
    spin_box.grid(column=6, row=1, sticky=E)

    # Add plus function, for addition material at storage.
    def increase_material_in_str():
        answer = msg.askyesno("Back to storage",
                              f"Are you sure that you want back {material_in_str.get()}"
                              f" item of material to the storage?")
        activator = True
        if answer == activator:

            try:
                storage_pickle = open("st1_storage.pickle", "rb")
                from_pickle = pickle.load(storage_pickle)
                total = from_pickle + material_in_str.get()

                with open("st1_storage.pickle", "wb") as w:
                    pickle.dump(total, w)

            except Exception as ex:
                print("Error during unpickling object (Possibly unsupported):", ex)
        else:
            msg.showinfo(title="Back to storage canceling",
                         message="Back to storage"
                                 "canceling you can back to work.")

    # Back to storage
    back_to_storage_label = Label(my_frame1, text="Back to storage")
    back_to_storage_label.grid(column=7, row=0)
    back_to_storage = Button(my_frame1, text="+")
    back_to_storage['command'] = increase_material_in_str
    back_to_storage.grid(column=7, row=1)
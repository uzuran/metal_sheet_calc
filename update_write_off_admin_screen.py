from tkinter import *


def show_who_write_off_admin(my_frame5, admin_screen):

    def update_write_off_admin_screen():
        load_write_off = open("write_off", "r")
        read_write_off = load_write_off.read()
        write_off_label.config(text=str(read_write_off))
        admin_screen.after(2500, update_write_off_admin_screen)

    load_write = open("write_off", "r")
    read_write = load_write.read()

    write_off_label = Label(my_frame5, fg="red")
    write_off_label['text'] = read_write
    write_off_label.grid(row=0)

    update_write_off_admin_screen()

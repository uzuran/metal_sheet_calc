from tkinter import *
import datetime


def show_who_write_off(my_frame5):
    tday = datetime.date.today()
    date = Label(my_frame5, text=str(tday))
    date.grid(row=0)

    date_time = datetime.datetime.now()

    date_time_l = Label(my_frame5, text=str(date_time.strftime("%X")))
    date_time_l.grid(row=0, column=1)

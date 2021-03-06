from tkinter import *
from tkinter import ttk
from st1_admin import st1_admin_line
from update_write_off_admin_screen import show_who_write_off_admin


def admin_screen_window(user_name_v):
    admin_screen = Toplevel()
    admin_screen.title("Steel sheet calculator.")

    # setting tkinter window size
    admin_screen.geometry("1000x600")
    admin_screen.title("Steel sheet calculator.")
    #admin_screen.iconbitmap('./assets/pythontutorial.ico')

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

    check_user = Label(admin_screen, text=str(user_name_label.capitalize()) + " Is log in now.",
                       fg="green",
                       font="Arial",

                       )
    check_user.pack(anchor="e")

    # <-- SCROLL BAR -->

    # Create a canvas.
    my_canvas = Canvas(admin_screen, width=150, height=40, bd=0, highlightthickness=0, relief='ridge')
    my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
    # Add scrollbar to the canvas.
    scroll_bar = Scrollbar(admin_screen, orient=VERTICAL, command=my_canvas.yview)
    scroll_bar.pack(side=RIGHT, fill=Y)
    # Configure the Canvas.
    my_canvas.config(yscrollcommand=scroll_bar.set)
    my_canvas.bind("<Configure>", lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))
    # Make new frame.
    second_frame = Frame(my_canvas)
    # Add a new frame to the  window in canvas
    my_canvas.create_window((0, 0), window=second_frame, anchor="nw")

    # MouseWheel
    def _on_mousewheel(event):
        my_canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    my_canvas.bind_all("<MouseWheel>", _on_mousewheel)

    # Add notebook of a materials to the second frame.
    notebook = ttk.Notebook(second_frame)
    notebook.pack()

    # Add frame options.
    frame_options = {"width": "500",
                     "height": "500"}

    my_frame1 = Frame(notebook, ** frame_options)
    my_frame2 = Frame(notebook, ** frame_options)
    my_frame3 = Frame(notebook, ** frame_options)
    my_frame4 = Frame(notebook, **frame_options)
    my_frame5 = Frame(notebook, **frame_options)

    # Add notebook on screen.
    notebook.add(my_frame1, text="Steel material")
    notebook.add(my_frame2, text="Aluminium material")
    notebook.add(my_frame3, text="Stainless steel material")
    notebook.add(my_frame4, text="Special material")
    notebook.add(my_frame5, text="Write off")

    st1_admin_line(my_frame1, admin_screen, user_name_v)
    show_who_write_off_admin(my_frame5, admin_screen)


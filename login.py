from tkinter import font
import PIL.Image
import PIL.ImageTk
import tkinter as tk
from tkinter import ttk


def loginScreen():

    window = tk.Tk()
    window.tk.call('source', './Forest-ttk-theme/forest-dark.tcl')
    ttk.Style().theme_use('forest-dark')

    # Custom colors
    bgcolor = "#333"
    white = "#fff"

    window.configure(background=bgcolor)
    window.minsize(800, 450)
    window.maxsize(800, 450)
    window.title("BDS-library")
    window.iconbitmap("./icons/vuticon.ico")

    pic = PIL.Image.open("./images/pepememe.png").resize(
        (200, 200), PIL.Image.ANTIALIAS)
    tkpic = PIL.ImageTk.PhotoImage(pic)
    label = ttk.Label(window, image=tkpic)
    label.pack()

    # Username
    usLabel = ttk.Label(window, text="Username", background=bgcolor, foreground=white,
                        font=("Arial", 15)).pack(pady=10)
    usEntry = ttk.Entry(window, width=25,).pack(pady=7.5)
    # Password
    pswLabel = ttk.Label(window, text="Password", background=bgcolor,
                         foreground=white, font=("Arial", 15)).pack(pady=10)
    pswEntry = ttk.Entry(window, width=25, show="*").pack(pady=7.5)
    # Submit
    subButton = ttk.Button(window, text="Submit", width=15).pack(
        side=tk.BOTTOM, pady=15)

    window.mainloop()

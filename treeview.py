from tkinter import font
import PIL.Image
import PIL.ImageTk
import tkinter as tk
from tkinter import ttk

class viewDatabase:
    # username, password
    def viewScreen():
        window = tk.Tk()
        window.tk.call('source', './Forest-ttk-theme/forest-dark.tcl')
        ttk.Style().theme_use('forest-dark')

        # Custom colors
        bgcolor = "#333"
        white = "#fff"

        window.configure(background=bgcolor)
        window.minsize(1200, 800)
        window.maxsize(1200, 800)
        window.title("Library treeview")
        window.iconbitmap("./icons/vuticon.ico")

        window.mainloop()

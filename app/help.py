from tkinter import *
from tkinter import ttk
from window import Window

import webbrowser

class Help():
  # Help window on in the 'User Info' window
  def displayHelp(self, window):
    windowAppearance = Window()

    # Opening a new window on top of our main window, setting the resolution and title
    popUp = Toplevel(window)
    windowAppearance.centerWindow(popUp, 400, 200)
    popUp.title("Help")

    # All the text labels are packed below each other
    infoLabel = ttk.Label(popUp, text="Did you actually expect help you peasant ?", font='bold').pack(anchor=CENTER, pady=15)
    idInfoLabel = ttk.Label(popUp, text="ID is automatically generated from database").pack(anchor=CENTER, pady=10)


  def importanceOfPS(self, popUp):
    def callback(url):
      webbrowser.open_new(url)

    windowAppearance = Window()
    # Deleting everything from the pop up window because we moved to a next window
    for widget in popUp.winfo_children():
          widget.destroy()
    # Setting the resolution and title
    windowAppearance.centerWindow(popUp, 600, 300)
    popUp.title("Help")
    # All the text labels are packed below each other
    infoLabel = ttk.Label(popUp, text="The importance of Prepared Statements: ", font='bold')
    textLabel = ttk.Label(popUp, text=
    """ 
    Prepared statements are used to deny the possibility of SQL injection attack.
    These attacks use the inputs that are used to retrieve data from any database
    by using special characters used in to end SQL querys or to produce an error
    that allows them to retrieve usefull information for further attacks.
    """)
    linkLabel = ttk.Label(popUp, text = "SQL injection attack example can be found")
    link = ttk.Label(popUp, text = "HERE", foreground="red")
      
    infoLabel.pack(anchor=CENTER, pady=15) 
    textLabel.pack(anchor=CENTER)
    linkLabel.pack(anchor=CENTER)
    link.pack(anchor=CENTER)
    
    link.bind("<Button-1>", lambda e:callback("https://www.hacksplaining.com/exercises/sql-injection#"))
from tkinter import *
from tkinter.constants import ACTIVE, CENTER, W
from typing import Collection
import PIL.Image
import PIL.ImageTk
import tkinter as tk
from tkinter import ttk

from dbOperations import dbOp
from viewOperations import viewOp
from help import Help

class viewDatabase:
    # username, password



    def viewScreen(self, nick):
        def openHelp():
            helpWindow = Help()
            helpWindow.displayHelp(wView)

        self.nick = nick
        self.role = dbOp.getRole(dbOp,self.nick)

        # Vytvoření okna
        wView = tk.Tk()
        wView .tk.call('source', './Forest-ttk-theme/forest-dark.tcl')
        ttk.Style().theme_use('forest-dark')

        menu = Menu(wView)

        # Help menu
        wView.config(menu=menu)
        helpMenu = Menu(menu)
        menu.add_cascade(label="Help", menu=helpMenu)
        helpMenu.add_command(label="Help", command=openHelp, background="white", foreground="black")

        # Custom colors
        bgcolor = "#333"
        
        #Konfigurace okna
        wView .configure(background=bgcolor)
        wView .minsize(900, 600)
        wView .maxsize(900, 600)
        wView .title("Library treeview")
        wView .iconbitmap("./icons/vuticon.ico")

        # Nastavení importovaného stylu
        ttk.Style().theme_use('forest-dark')
        style = ttk.Style()

        # Změna barvy při označení
        style.map('Treeview',background=[('selected', "#c22740")])

        # Creating the frame of our treeview
        treeFrame = Frame(wView)
        treeFrame.pack(pady=10)

      # Creating a scrollbar
        scroll = ttk.Scrollbar(treeFrame)
        scroll.pack(side=RIGHT, fill=Y)

        # Vytvoření treeview
        dataTree = ttk.Treeview(treeFrame , selectmode="extended")
        dataTree.pack(pady=10, fill=BOTH)

        # Config of our scrollbar
        scroll.config(command=dataTree.yview)

        # Definování sloupců
        dataTree['columns'] = ("ID", "name", "nick", "mail",  "phoneNum", "transactions", "role")

        # Formátování sloupců
        dataTree.column("#0", width=0, stretch = NO)
        dataTree.column("ID", anchor=W, width=50)
        dataTree.column("name", anchor=W, width=120)
        dataTree.column("nick", anchor=W, width=70)
        dataTree.column("mail", anchor=W, width=200)
        dataTree.column("phoneNum", anchor=W, width=90)
        dataTree.column("transactions", anchor=W, width=80)
        dataTree.column("role", anchor=W, width=60)
        # Nadpisy
        dataTree.heading("#0", text="", anchor=W)
        dataTree.heading("ID", text="ID", anchor=W)
        dataTree.heading("name", text="Name", anchor=W)
        dataTree.heading("nick", text="Nick", anchor=W)
        dataTree.heading("mail", text="Email", anchor=W)
        dataTree.heading("phoneNum", text="Phone num.", anchor=W)
        dataTree.heading("transactions", text="Price ($)", anchor=W)
        dataTree.heading("role", text="Role", anchor=W)
        
        #Označení řádků (lichý/sudý) pro lepší orientaci
        dataTree.tag_configure('oddrow', background="#575757")
        dataTree.tag_configure('evenrow', background="#2A2A2A")
        

        filterL = Label(wView, text="Filter by Last name")
        filterE = Entry(wView, width=20)
        filterSub = Button(wView)

        # Pokud je role customer
        if(self.role == 'customer'):
            dbOp.getCustomer(dbOp, dataTree,self.nick)  

        # Pokud je role employee
        if(self.role == 'employee'):
            dbOp.getAll(dbOp,dataTree)
            viewOp.showFilter(wView, dataTree)
            
        # Pokud je role admin
        if(self.role == 'admin'):
            dbOp.getAll(dbOp, dataTree)
            viewOp.showFilter(wView, dataTree)
            viewOp.showAdmin(viewOp,wView, dataTree)

        wView.mainloop()



## Custom buttons
            #addButton  

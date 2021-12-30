from tkinter import *
from tkinter.constants import ACTIVE, CENTER, W
from typing import Collection
import PIL.Image
import PIL.ImageTk
import tkinter as tk
from tkinter import ttk

from dbOperations import dbOp

class viewDatabase:
    # username, password
    def viewScreen(self, nick):
        self.nick = nick
        self.role = dbOp.getRole(dbOp,self.nick)

        # Vytvoření okna
        wView = tk.Tk()
        wView .tk.call('source', './Forest-ttk-theme/forest-dark.tcl')
        ttk.Style().theme_use('forest-dark')

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

        # Vytvoření treeview
        my_tree = ttk.Treeview(wView , selectmode="extended")
        my_tree.pack(pady=50)

        # Definování sloupců
        my_tree['columns'] = ("ID", "name", "nick", "mail",  "phoneNum", "transactions", "role")

        # Formátování sloupců
        my_tree.column("#0", width=0, stretch = NO)
        my_tree.column("ID", anchor=CENTER, width=50)
        my_tree.column("name", anchor=CENTER, width=120)
        my_tree.column("nick", anchor=CENTER, width=70)
        my_tree.column("mail", anchor=CENTER, width=200)
        my_tree.column("phoneNum", anchor=CENTER, width=90)
        my_tree.column("transactions", anchor=CENTER, width=80)
        my_tree.column("role", anchor=CENTER, width=60)

        # Nadpisy
        my_tree.heading("#0", text="", anchor=CENTER)
        my_tree.heading("ID", text="ID", anchor=CENTER)
        my_tree.heading("name", text="Name", anchor=CENTER)
        my_tree.heading("nick", text="Nick", anchor=CENTER)
        my_tree.heading("mail", text="Email", anchor=CENTER)
        my_tree.heading("phoneNum", text="Phone num.", anchor=CENTER)
        my_tree.heading("transactions", text="Price ($)", anchor=CENTER)
        my_tree.heading("role", text="Role", anchor=CENTER)

        # Označení řádků (lichý/sudý) pro lepší orientaci
        my_tree.tag_configure('oddrow', background="white")
        my_tree.tag_configure('evenrow', background="#f78396")
        
        # Pokud je role customer
        if(self.role == 'customer'):
            customerInfo = dbOp.getCustomer(dbOp, self.nick)
            my_tree.insert(parent='', index='end', iid=0, text='', 
            values=(customerInfo[0], customerInfo[1]+" "+ customerInfo[2],  customerInfo[3], customerInfo[4], customerInfo[5], customerInfo[6], customerInfo[7]))
        # Pokud je role employee
        # if(self.role == 'employee'):
            # employeeInfo = dbOp.getAll(dbOp, self.nick)
        # Pokud je role admin
        if(self.role == 'admin'):
            add_frame = Frame(wView )
            add_frame.pack(pady=10)

            firstNaL = Label(add_frame, text="First Name ")
            lastNaL = Label(add_frame, text = "Last Name")
            nickL = Label(add_frame, text="Nick")
            mailL = Label(add_frame, text="Email")
            phoneL = Label(add_frame, text="Phone")
            roleL = Label(add_frame, text="Role")

            firstNaEn = Entry(add_frame, width= 20)
            lastNaEn = Entry(add_frame, width= 20)
            nickEn = Entry(add_frame, width= 10)
            mailEn = Entry(add_frame, width=30)
            phoneEn = Entry(add_frame, width= 15)
            roleEn = Entry(add_frame, width= 10)

            ## Custom buttons
            #addButton
            #removeAll
            #filter

            ## Right click menu
            # Remove
            # Edit
            # 

            firstNaL.grid(row=0, column=0)
            lastNaL.grid(row=0, column=1)
            nickL.grid(row=0, column=2)
            mailL.grid(row=0, column=3)
            phoneL.grid(row=0, column=4)
            roleL.grid(row=0, column=5)

            firstNaEn.grid(row=1, column=0)
            lastNaEn.grid(row=1, column=1)
            nickEn.grid(row=1, column=2)
            mailEn.grid(row=1, column=3)
            phoneEn.grid(row=1, column=4)
            roleEn.grid(row=1, column=5)
        

        wView.mainloop()



viewDatabase.viewScreen(viewDatabase, 'Walker')
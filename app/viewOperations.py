from tkinter import *
from tkinter.constants import ACTIVE, CENTER, W
import PIL.Image
import PIL.ImageTk
import tkinter as tk
from tkinter import ttk

from dbOperations import dbOp


class viewOp:
    # Funkce zobrazí pole a button pro filtrování
    def showFilter(window, tree):
        def getFilterName():
            return filterE.get()

        filterL = Label(window, text="Filter by Last name")
        filterE = Entry(window, width=20)
        filterSub = Button(window, background="#666", width=17, text='Submit', command= lambda: dbOp.filterName(dbOp, getFilterName(), tree))

        filterL.pack()
        filterE.pack(pady=5)
        filterSub.pack()

    
    # Funkce která zobrazí funkce přístupné jen pro uživatele s rolí admin
    ## Většina těchto funkcí jsou volány při zmáčknutí tlačítek
    def showAdmin(self, window, tree):
        def getfName():
            return firstNaEn.get()
        def getlName():
            return lastNaEn.get()
        def getNick():
            return nickEn.get()
        def getMail():
            return mailEn.get() 
        def getPhone():
            return phoneEn.get()
        def getRole():
            return roleEn.get()
            
        # Funkce, která vymaže všechno v input polích
        def clearBoxes(): 
            firstNaEn.delete(0, END)
            lastNaEn.delete(0, END)
            nickEn.delete(0, END)
            mailEn.delete(0, END)
            phoneEn.delete(0, END)
            roleEn.delete(0, END)

        # Funkce, která resetuje celé okno
        def resetTree(tree):
            dbOp.clearTree(tree)
            dbOp.getAll(dbOp, tree)
            clearBoxes()

        # Funkce pro přidání osob 
        def addingRecord(ID, fName, lName, nick, mail, phone, role):
            dbOp.addRecord(ID, fName, lName, nick, mail, phone, role)
            resetTree(tree)
        # Funkce pro odebrání osob
        def removeRecord(tree):
            id = tree.selection()
            dbOp.removingRecord(id[0])
            resetTree(tree)
        # Funkce pro edit osob
        def editRecord(tree):
            ID = tree.selection()
            record = dbOp.updateRecord(ID[0])

            firstNaEn.insert(0, record[0])
            lastNaEn.insert(0, record[1])
            nickEn.insert(0, record[2])
            mailEn.insert(0, record[3])
            phoneEn.insert(0, record[4])
            roleEn.insert(0, record[5])
            # dbOp.updateRecord(ID)

        #Frame pro popisky a input pole 
        add_frame = Frame(window)
        add_frame.pack(pady=10)
        #Frame pro tlačítka
        action_frame = Frame(window)
        action_frame.pack(pady=10)

        # Label a Entry pole
        firstNaL = Label(add_frame, text="First Name")
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
        
        # Funkční tlačítka
        ediBtn = Button(action_frame, text="Edit", width=10, command= lambda: editRecord(tree))
        selBtn = Button(action_frame, text="Select", width=10, command= clearBoxes())
        resBtn = Button(action_frame, text="Reset", width=10, command= lambda: resetTree(tree))
        addBtn = Button(action_frame, text="Add", width=10, command= lambda: addingRecord(dbOp.getNextID(), getfName(), getlName(), getNick(), mailEn.get() , phoneEn.get(), roleEn.get()))
        remBtn = Button(action_frame, text="Remove", width=10, command= lambda: removeRecord(tree))

        ediBtn.grid(row=0, column= 0)
        selBtn.grid(row=0, column= 1)
        resBtn.grid(row=0, column= 2)
        addBtn.grid(row=0, column= 3)
        remBtn.grid(row=0, column= 4)
from tkinter import font
from tkinter import ttk
import tkinter as tk
import PIL.ImageTk
import PIL.Image
# Databáze
from dbOperations import dbOp
from treeview import viewDatabase

class login:
    def loginScreen():

    # Vlastní funkce
        #-> Zobrazí error zprávu, zamezuje zobrazování více zpráv po dalším zmáčknutí tlačitka
        def invalidLogin(self, invalidLabel):
            self.invalidLabel = invalidLabel
            if invalidLabel.winfo_exists() == False:
                # Pokud je error zpráva viditelná, příkaz ignoruje
                return 0
            else:
                # Zobrazí error zprávu
                invalidLabel.pack()

        #--> Validuje login
        def loginValidation(self, username, password, window, invalidLabel):
            self.username = username
            self.password = password
            
            print("-login-")
            print(username)
            print(self.username)
            # Nahrajeme hodnoty z polí do proměnné
            # Funkce ze třídy dbOp (dbOperations.py), která se připojí k databázi, vyhledá uživatele podle přezdívky (nick) a porovná
            # hash, který je vypočítán z hesla s hashem uloženým v databázi.
            if dbOp.dbValidation(dbOp, self.username, self.password):
                window.destroy()
                viewDatabase.viewScreen()
                # username, password
            else:
                invalidLogin(login,invalidLabel)

    # Custom colors
        bgcolor = "#333"
        white = "#fff"
    # Window init
        window = tk.Tk()
    # Nastavení theme
        window.tk.call('source', './Forest-ttk-theme/forest-dark.tcl')
        ttk.Style().theme_use('forest-dark')
    # Window config
        window.configure(background=bgcolor)
        window.minsize(600, 450)
        window.maxsize(600, 450)
    # Title
        window.title("Library login")
    # Favicon
        window.iconbitmap("./icons/vuticon.ico")
    # Login Image
        pic = PIL.Image.open("./images/pepememe.png").resize((200, 200), PIL.Image.ANTIALIAS)
        tkpic = PIL.ImageTk.PhotoImage(pic)
        label = ttk.Label(window, image=tkpic).pack(pady=10)
    # Username [Popis + Pole] + proměnná pro získání hodnoty z proměnné
        usLabel = ttk.Label(window, text="Username", background=bgcolor,foreground=white, font=("Arial", 13)).pack(pady=5)
        usEntry = ttk.Entry(window, width=25)
        username = usEntry.get()
        usEntry.pack(pady=5)
    # Password [Popis + Pole]
        pswLabel = ttk.Label(window, text="Password", background=bgcolor,foreground=white, font=("Arial", 13)).pack(pady=5)
        pswEntry = ttk.Entry(window, width=25, show="*")
        password = pswEntry.get()
        pswEntry.pack(pady=5)
    # Error message (Musí být nad submit buttonem, protože invalidLabel je argument pro funkci, kterou používá submit button)
        invalidLabel = ttk.Label(window, text=" Incorrect credentials ", foreground="#ff5733")
    # Submit
        # subButton = ttk.Button(window, text="Submit",width=24, command=lambda: invalidLabel(invalidLabel))
        subButton = ttk.Button(window, text="Submit",width=24, command=lambda: loginValidation(login, username, password, window, invalidLabel))
        subButton.pack(pady=10)

        window.mainloop()

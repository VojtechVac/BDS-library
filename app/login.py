
from tkinter import font
from tkinter import ttk
import tkinter as tk
## Tkinter konstanty pro pack()
from tkinter.constants import BOTTOM, CENTER, N
import PIL.ImageTk
import PIL.Image
# Databáze
from dbOperations import dbOp
from treeview import viewDatabase

class login:
    def loginScreen():
    # Custom colors
        bgcolor = "#333"
        white = "#fff"

    # Vlastní funkce
        def closeWindow(self, window):
            self.window = window
            (self.window).destroy()

        #-> Zobrazí error zprávu
        def invalidLogin(self, invalidLabel):
            self.invalidLabel = invalidLabel
            wError = tk.Toplevel(wLogin)
            wError.configure(background=bgcolor)
            wError.maxsize(300, 200)
            wError.title("Login Error")

            message = ttk.Label(wError, text = "Username / Password is wrong !", foreground="#ff5733", background=bgcolor, font=("Arial", 14))
            message.pack(pady=40, anchor=N)
            exitButton = ttk.Button(wError, text="Okay!", width=25,command=lambda: closeWindow(login,wError))
            exitButton.pack(anchor=CENTER)

            if invalidLabel.winfo_exists() == False:
                # Pokud je error zpráva viditelná, příkaz ignoruje
                return False
            else:
                # Zobrazí error zprávu
                message = ttk.Label(wError, text = "Username / Password is wrong !", foreground="#ff5733", background=bgcolor, font=("Arial", 14))
                message.pack(pady=40, anchor=N)
                exitButton = ttk.Button(wError, text="Okay!", width=25,command=lambda: closeWindow(login,wError))
                exitButton.pack(anchor=CENTER)
                invalidLabel.pack(pady=10)
        # Funkce pro získání hodnoty username z entry pole       
        def getUsername():
            username = usEntry.get()
            return username

        # Funkce pro získání hodnoty password z entry pole       
        def getPassword():
            password = pswEntry.get()
            return password

        #--> Validuje login
        def loginValidation(self, window, invalidLabel):
            self.username = getUsername()
            self.password = getPassword()
            
            # Nahrajeme hodnoty z polí do proměnné
            # Funkce ze třídy dbOp (dbOperations.py), která se připojí k databázi, vyhledá uživatele podle přezdívky (nick) a porovná
            # hash, který je vypočítán z hesla s hashem uloženým v databázi.

            if (dbOp.dbValidation(dbOp, self.username, self.password)):
                closeWindow(login, window)
                viewDatabase.viewScreen(viewDatabase,self.username)
            else:
                invalidLogin(login,invalidLabel)

    
    # Window init
        wLogin = tk.Tk()
    # Nastavení theme
        wLogin.tk.call('source', './Forest-ttk-theme/forest-dark.tcl')
        ttk.Style().theme_use('forest-dark')

    # Window config
        wLogin.configure(background=bgcolor)
        wLogin.minsize(700, 450)
        wLogin.maxsize(700, 450)
    # Title
        wLogin.title("Library login")
    # Favicon
        wLogin.iconbitmap("./icons/vuticon.ico")
    # Login Image
        pic = PIL.Image.open("./images/fekt_icon.png").resize((600,120), PIL.Image.ANTIALIAS)
        tkpic = PIL.ImageTk.PhotoImage(pic)
        label = ttk.Label(wLogin, image=tkpic).pack(pady=30)
    # Username [Popis + Pole] + proměnná pro získání hodnoty z proměnné
        usLabel = ttk.Label(wLogin, text="Username", background=bgcolor,foreground=white, font=("Arial", 13)).pack(pady=5)
        usEntry = ttk.Entry(wLogin, width=25)
        usEntry.pack(pady=5)
    # Password [Popis + Pole]
        pswLabel = ttk.Label(wLogin, text="Password", background=bgcolor,foreground=white, font=("Arial", 13)).pack(pady=5)
        pswEntry = ttk.Entry(wLogin, width=25, show="*")
        pswEntry.pack(pady=5)
    # Error message (Musí být nad submit buttonem, protože invalidLabel je argument pro funkci, kterou používá submit button)
        invalidLabel = ttk.Label(wLogin, text=" Incorrect credentials ", foreground="#ff5733")
    # Submit
        subButton = ttk.Button(wLogin, text="Submit",width=24, command=lambda: loginValidation(login, wLogin, invalidLabel))
        subButton.pack(pady=10)

    # Copyright
        cpLabel = ttk.Label(wLogin, text="©VojtechVac")
        cpLabel.pack(side=BOTTOM, pady=7.5)

        wLogin.mainloop()

from tkinter import *
from tkinter.constants import ACTIVE, CENTER, W
import PIL.Image
import PIL.ImageTk
import tkinter as tk
from tkinter import ttk

import dbOperations

class roles:

    #Role customer [Zákazník]
    class customer:
        def loadCustomer(self, window, nick):
            self.nick = nick
            customerInformation = (dbOperations.dbOp.showCustomer(dbOperations.dbOp, self.nick))

            
    # #Role employee [Zaměstnanec]    
    # class employee:

    # #Role admin
    # class admin:
        


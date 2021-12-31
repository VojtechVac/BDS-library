# Import modulu pro Login
from login import login

# Import modulu pro zobrazení databáze (Pouze pro testování)
# from treeview import viewDatabase

# Voláme funkci loginScreen() ze třídy login (login.py), která program "zapne".
login.loginScreen()

# # Volání funkce viewScreen() ze třídy viewDatabase (treeview.py), užívá se pouze pro testování (přeskočení loginu)
# viewDatabase.viewScreen()

# Tato funkce nám dá možnost přihlášení, pokud použijeme špatné přihlašovací údaje, program nás na ně upozorní a nepustí nás dál.
# V případě zadání správných údajů je ve funkci loginScreen() zavolána funkce z třídy viewDatabase (treeview.py) jménem viewScreen().
# Proto je v této tříde je zapotřebí zavolat pouze jednu funkci.
# BDS-library

# Autor:   Vojtěch Vaculík <*VojtechVac*> 
# Předmět: BDS - Bezpečnost Databázových Systémů
# Ročník : BPC-IBE 2

# Úvod:

Zadání projektu, které lze nalézt v poslední části tohoto souboru společně s checklistem, bylo vypracováno na ***[]%***.

Projekt navazuje na předešlé projekty, které pojednávali o návrhu databáze a prácí s ní.
Cílem projektu je vytvořit vytvořit funkční aplikace, která implementuje vytvořenou databázi
z předešlého projektu za pomoci několika externích knihoven. [Bcrypt, Psycopg2, PyCryptodome]

Aplikace musí mít grafické rozhraní (GUI), které umožní uživateli autentifikaci za pomocí
přihlašovacích údajů. Při neúspěšné autentifikaci vyskočí pop-up window s error zprávou.
V případě úspěšného přihlášení aplikace umožní uživateli zobrazit data o knihách, transakcích
a událostech. Dle role bude mít uživatel k dispozici různé nástroje pro práci s těmito daty.

Všichni uživatelé mají možnost filtrovat data podle daného parametru, uživatelé s vyšší autorizací
mohou data upravovat, mazat a nebo přidávat. K dispozici budou také externí tlačítka po okrajních
lištách aplikace. Tyto tlačítka budou nabízet možnosti HELP, SQL Injection, Dummy table.

Aplikace mít logovací protokol, který bude zapisovat chyby, které mohli vzniknout ze vstupu uživatele.
Zároveň také bude o půlnoci automaticky zálohována za pomocí zálohovací funkce MidnightBackup


# Technický popis:

# Checklist R[6/15] O[1/7] [TOTAL *7/22 -> 31,8%*]

##  [✓] - Implementing desktop application in Java or Python.

..##   [X] - Compilable and runnable from the command-line. [py main.py]

##  [✓] - Database will containt user passwords in a hash form. [Hashed by *Bcrypt*]

##  [✓] - Sign-In window with username / password authentication. (If wrong, error pop-up window)

##  [✓] - Create a database user role for the application. (Not superuser role) 

.##  [X] - For at least one entity implement CRUD. (create,read,update,delete) 
.##         Include for one entity the findAll operation.

.##  [X] - Detailed view for one entity.

..##  [X] - Implement one operation in GUI that invokes more than one query and run them all in one
..##          transaction. (If wrong, rollback)

.##  [X] - Provide filter. (ex.: find and order by last_name) 

..##  [X] - Creating dummy table. Creating GUI window for SQL Injection attack simulation.
..###               - Explain the necessity of prepared statements.

..##  [X] - Midnight backup script.
    
..##  [X] - Logging suitable exceptions.
    
##  [✓] - Create GitHub repository for your project. Include README with program description. (Commits >= 5)
    
##  [✓] - Add licence file with suitable licence. [MIT]
    
##  [✓] - Create / Generate document with all external libraries listed with their licence.
    
##  [X] (O) - Encrypt selected database columns. [PyCryptodome]
    
##  [X] (O) - Use arbitrary method to retrieve data and show them via GUI.
    
..##  [X] (O) - Generate self-signed certificate for your Database / App.
    
##  [✓] (O) - Generate SSH-Keys and configure your GitHub account to be able to use SSH. 
##              Set remote-url origion of your project to use SSH
    
##  [X] (O) - Implement the JUnit test for selected database queries.
    
##  [X] (O) - Dockerize your project.
    
##  [X] (O) - Integrate GitHub Actions for your project to check the build / test phase.
    
   
# Závěr:    

Aplikace, a k ní příslušící projektové dokumenty byly vypracovány v rámci vysokoškolského projektu 
Autor : Vojtěch Vaculík <VojtechVac>
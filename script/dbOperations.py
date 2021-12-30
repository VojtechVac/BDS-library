# Kryptografická knihovna
from tkinter.constants import FALSE
import bcrypt
# Používá se pro práci s POSTGRESQL
import psycopg2


class dbOp:
    # Globální proměnné
    global DB_HOST
    global DB_NAME
    global DB_USER
    global DB_PASS
    global DB_PORT
    # Konfigurační hodnoty pro připojení k databázi
    DB_HOST = "localhost"
    DB_NAME = "library"
    DB_USER = "postgres"
    DB_PASS = "postgres"
    DB_PORT = 5432

    # Validace přihlašovacích údajů
    def dbValidation(self, username, password):
        self.username = username    
        self.password = password
        # self.hashedPassword = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

        connection = psycopg2.connect(
            user        =DB_USER,
            dbname      =DB_NAME,
            password    =DB_PASS,
            host        =DB_HOST,
            port        =DB_PORT
        ) 

        cursor = connection.cursor()
        cursor.execute("SELECT hashed_password FROM Public.user WHERE nick= %s", [self.username])
        hashed = cursor.fetchall()
        if(cursor.rowcount == 0):
            return False
        else:
            result = str(hashed[0][0])
            cursor.close()
            connection.close()
            if bcrypt.checkpw(self.password.encode(), result.encode()):
                return True
            else:
                return False
    #Vrátí roli přihlášeného uživatele
    def getRole(self, nick):
        self.nick = nick
        
        connection = psycopg2.connect(
            user        =DB_USER,
            dbname      =DB_NAME,
            password    =DB_PASS,
            host        =DB_HOST,
            port        =DB_PORT
        ) 
        cursor = connection.cursor()
        cursor.execute("SELECT r.role_type FROM public.user u RIGHT JOIN public.role r ON u.user_id = r.role_id WHERE u.nick= %s", [self.nick])
        role = cursor.fetchall()
        return role[0][0]

    def getCustomer(self, nick):
        self.nick = nick

        connection = psycopg2.connect(
            user        =DB_USER,
            dbname      =DB_NAME,
            password    =DB_PASS,
            host        =DB_HOST,
            port        =DB_PORT
        )
        cursor = connection.cursor()

        cursor.execute("SELECT user_id FROM Public.user WHERE nick = %s", [self.nick])
        user_id = cursor.fetchone()

        cursor.execute(
            """
            SELECT u.user_id, u.first_name, u.last_name, u.nick, c.mail, c.phone , t.price, r.role_type
            FROM public.user u JOIN public.contact c ON u.user_id=c.user_id JOIN public.role r ON u.user_id = r.role_id
            JOIN public.transactions t ON u.user_id = t.user_id
            WHERE u.user_id = %s
            """, [user_id])
        #Vrací tuple s informacema, index 0 - 7
        customer = cursor.fetchall()
        return customer[0]
        
    # def showAll():


# customerInfo = dbOp.showCustomer(dbOp, 'Kibi')
# print(f" ID: {customerInfo[0]} \n Name: {customerInfo[1]} {customerInfo[2]} \n Nick: {customerInfo[3]} \n Email: {customerInfo[4]} | Phone: {customerInfo[5]} \n Role: {customerInfo[6]}")


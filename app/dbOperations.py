# Kryptografická knihovna
from os import closerange
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
        
        cursor.close()
        connection.close()

        return role[0][0]

    def getCustomer(self, dataTree, nick):
        self.nick = nick

        connection = psycopg2.connect(
            user        =DB_USER,
            dbname      =DB_NAME,
            password    =DB_PASS,
            host        =DB_HOST,
            port        =DB_PORT
        )
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT DISTINCT u.user_id, u.first_name, u.last_name, u.nick, c.mail, c.phone , t.price, r.role_type
            FROM public.user u JOIN public.contact c ON u.user_id=c.user_id JOIN public.role r ON u.user_id = r.role_id
            JOIN public.transactions t ON u.user_id = t.user_id
            WHERE u.nick = %s
            """, [self.nick])
        #Vrací tuple s informacema, index 0 - 7
        customer = cursor.fetchall()
        customerRecord = customer[0]

        cursor.close()
        connection.close()


        dataTree.insert(parent='', index='end', iid=0, text='', values=(customerRecord[0], customerRecord[1]+" "+ customerRecord[2],  customerRecord[3], customerRecord[4], customerRecord[5], customerRecord[6], customerRecord[7]))
        
        
    def getAll(self,tree):
        connection = psycopg2.connect(
            user        =DB_USER,
            dbname      =DB_NAME,
            password    =DB_PASS,
            host        =DB_HOST,
            port        =DB_PORT
        )
        cursor = connection.cursor()
        cursor.execute("""
        SELECT DISTINCT u.user_id, u.first_name, u.last_name, u.nick, c.mail, c.phone, t.price, ro.role_type
        FROM public.user u LEFT JOIN public.contact c ON u.user_id = c.user_id
        LEFT JOIN public.transactions t ON t.user_id = u.user_id
        LEFT JOIN public.user_has_address a ON u.user_id = a.user_id
        LEFT JOIN public.address ad ON a.address_id = ad.address_id
        LEFT JOIN public.user_has_role r ON r.user_id = u.user_id
        LEFT JOIN public.role ro ON r.role_id = ro.role_id
		ORDER by user_id ASC""")
        records = cursor.fetchall()
        
        global count
        count = 0
          # For loop to differentiate odd rows and even rows based on tags 'oddrow' and 'evenrow'
        for record in records:
            if count % 2 == 0:
              tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1]+" "+record[2], record[3], record[4], record[5], record[6], record[7]), tags=('evenrow',))
            else:
              tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1]+" "+record[2], record[3], record[4], record[5], record[6], record[7]), tags=('oddrow',)) 
            count += 1

        cursor.close()
        connection.close()
    

    def clearTree(tree):
        for item in tree.get_children():
            tree.delete(item)

    def filterName(self, last_name, tree):
        self.last_name = last_name

        dbOp.clearTree(tree)

        if(self.last_name == ""):
            dbOp.getAll(dbOp, tree)
        
        connection = psycopg2.connect(
            user        =DB_USER,
            dbname      =DB_NAME,
            password    =DB_PASS,
            host        =DB_HOST,
            port        =DB_PORT
        )
        cursor = connection.cursor()
        cursor.execute("""
        SELECT DISTINCT u.user_id, u.first_name, u.last_name, u.nick, c.mail, c.phone, t.price, ro.role_type
        FROM public.user u LEFT JOIN public.contact c ON u.user_id = c.user_id
        LEFT JOIN public.transactions t ON t.user_id = u.user_id
        LEFT JOIN public.user_has_address a ON u.user_id = a.user_id
        LEFT JOIN public.address ad ON a.address_id = ad.address_id
        LEFT JOIN public.user_has_role r ON r.user_id = u.user_id
        LEFT JOIN public.role ro ON r.role_id = ro.role_id
        WHERE u.last_name = %s""", [self.last_name])
        records = cursor.fetchall()
        global count
        count = 0
          # For loop to differentiate odd rows and even rows based on tags 'oddrow' and 'evenrow'
        for record in records:
            if count % 2 == 0:
              tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1]+" "+record[2], record[3], record[4], record[5], record[6], record[7]), tags=('evenrow',))
            else:
              tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1]+" "+record[2], record[3], record[4], record[5], record[6], record[7]), tags=('oddrow',)) 
            count += 1

    def getNextID():
        connection = psycopg2.connect(
            user        =DB_USER,
            dbname      =DB_NAME,
            password    =DB_PASS,
            host        =DB_HOST,
            port        =DB_PORT
        )
        cursor = connection.cursor()
        cursor.execute("""SELECT user_id
                            FROM public.user
                            order by user_id desc
                            limit 1
                        """)
        nextID = cursor.fetchone()
        nextID = int(nextID[0])
        return nextID + 1

    def addRecord(ID, fName, lName, nick, mail, phone, role):

        if role == "admin":
          role = 1
        elif role == "employee":
          role = 3
        elif role == "customer":
          role = 5

        connection = psycopg2.connect(
            user        =DB_USER,
            dbname      =DB_NAME,
            password    =DB_PASS,
            host        =DB_HOST,
            port        =DB_PORT
        )
        cursor = connection.cursor()
        
        cursor.execute("""INSERT INTO public.user (user_id, first_name, last_name, nick) VALUES (%s, %s, %s, %s);""", (ID, fName, lName, nick))
        cursor.execute("""INSERT INTO public.contact (user_id, mail, phone) VALUES (%s, %s, %s);""",(ID, mail, phone))
        cursor.execute("""INSERT INTO public.user_has_role (user_id, role_id) VALUES (%s, %s);""",(ID, role))
        connection.commit()

        cursor.close()
        connection.close()

    def removingRecord(ID): 
        connection = psycopg2.connect(
            user        =DB_USER,
            dbname      =DB_NAME,
            password    =DB_PASS,
            host        =DB_HOST,
            port        =DB_PORT
        )
        cursor = connection.cursor()
        
        # cursor.execute("""SELECT DISTINCT user_id FROM public.user WHERE nick = %s""", [nick])
        # id = cursor.fetchall()
        # print(id)

        cursor.execute("""DELETE FROM public.user_has_address WHERE user_id = %s""", (ID,))
        cursor.execute("""DELETE FROM public.user_has_role WHERE user_id = %s""", (ID,))
        cursor.execute("""DELETE FROM public.contact WHERE user_id = %s""", (ID,))
        cursor.execute("""DELETE FROM public.user WHERE user_id = %s""", (ID,))
        cursor.execute("""DELETE FROM public.transactions WHERE user_id = %s""", (ID,))
        connection.commit()
        cursor.close()
        connection.close()

    def getRecord(ID):
        connection = psycopg2.connect(
            user        =DB_USER,
            dbname      =DB_NAME,
            password    =DB_PASS,
            host        =DB_HOST,
            port        =DB_PORT
        )
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT u.user_id, u.first_name, u.last_name, u.nick, c.mail, c.phone , r.role_type
            FROM public.user u 
            JOIN public.contact c ON u.user_id=c.user_id 
            JOIN public.role r ON u.user_id = r.role_id
            WHERE u.user_id = %s """, [ID,])

        record = cursor.fetchall()
        cursor.close()
        connection.close()

        return record
        
        

    def updateRecord(ID):

        connection = psycopg2.connect(
            user        =DB_USER,
            dbname      =DB_NAME,
            password    =DB_PASS,
            host        =DB_HOST,
            port        =DB_PORT
        )
        cursor = connection.cursor()

        cursor.execute("""SELECT u.user_id, u.first_name, u.last_name, u.nick, c.mail, c.phone , r.role_type
                            FROM public.user u 
                            JOIN public.contact c ON u.user_id=c.user_id 
                            JOIN public.role r ON u.user_id = r.role_id
                            WHERE u.user_id = %s """, [ID,])
        record = cursor.fetchall()
        # print(record[0])

        # if role == "admin":
        #   role = 1
        # elif role == "employee":
        #   role = 3
        # elif role == "customer":
        #   role = 5

        # cursor.execute("""UPDATE public.user_has_role SET role_id= %s WHERE user_id= %s""", (role, ID))
        # cursor.execute("""UPDATE public.contact SET mail = %s, phone = %s WHERE user_id = %s""", (mail, phone, ID,))
        # cursor.execute("""UPDATE public.user SET first_name = %s, last_name = %s, nick = %s WHERE user_id = %s""", (fName, lName, nick, ID,))
        # connection.commit()
        # cursor.close()
        # connection.close()
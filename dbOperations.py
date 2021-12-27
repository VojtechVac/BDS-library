# Kryptografická knihovna
import bcrypt
# Používá se pro práci s POSTGRESQL
import psycopg2


class dbOp:
    # Validace přihlašovacích údajů
    def dbValidation(self, username, password):
        self.username = str(username)
        self.password = str(password)
        self.hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

        # Konfigurační hodnoty pro připojení k databázi
        DB_HOST = "localhost"
        DB_NAME = "library"
        DB_USER = "postgres"
        DB_PASS = "postgres"
        DB_PORT = 5432

        connection = psycopg2.connect(
            user        =DB_USER,
            dbname      =DB_NAME,
            password    =DB_PASS,
            host        =DB_HOST,
            port        =DB_PORT
        ) 
        
        cursor = connection.cursor()
        # cursor.execute("SELECT hashed_password FROM Public.user WHERE nick= %s ORDER BY user_id ASC", [self.username])
        # cursor.execute("SELECT password FROM Public.user WHERE nick=:username", {'username': self.username})
        cursor.execute("SELECT hashed_password FROM Public.user WHERE nick= 'Kibi'") #, (self.username)
        hashed = cursor.fetchall()
        if hashed == None:
            print("nenašel nic")
        else:
            print(hashed)


        # result = hashed[0][4]
        # print(result)
        # Testování - troubleshooting protože bcrypt je strašně dementní věc
        # print("---")
        # print(type(hashed))
        # print(hashed)
        # print("---")
        cursor.close()
        connection.close()

        # if bcrypt.checkpw(self.password.encode(), result.encode()):
        #     return True
        # else:
        #     return False

            
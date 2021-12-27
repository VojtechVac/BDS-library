# Kryptografická knihovna
import bcrypt
# Používá se pro práci s POSTGRESQL
import psycopg2


class dbOp:
    # Validace přihlašovacích údajů
    def dbValidation(self, username, password):
        self.username = username    
        self.password = password
        self.hashedPassword = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

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
        cursor.execute("SELECT hashed_password FROM Public.user WHERE nick= %s", [self.username])
        hashed = cursor.fetchall()
        result = str(hashed[0][0])
              
        cursor.close()
        connection.close()

        if bcrypt.checkpw(self.password.encode(), result.encode()):
            return True
        else:
            return False

            
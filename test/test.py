# Kryptografická knihovna
import bcrypt
# Používá se pro práci s POSTGRESQL
import psycopg2

DB_HOST = "localhost"
DB_NAME = "library"
DB_USER = "postgres"
DB_PASS = "postgres"
DB_PORT = 5432


conn = psycopg2.connect(
    user=DB_USER,
    dbname=DB_NAME,
    password=DB_PASS,
    host=DB_HOST,
    port=DB_PORT
)

cursor = conn.cursor()

cursor.execute(
    """
    SELECT hashed_password FROM Public.user WHERE nick = 'item=?'",(self.nick)
    """
)

rows = cursor.fetchall
print(rows())
password = 'passw'



cursor.close()
conn.close()



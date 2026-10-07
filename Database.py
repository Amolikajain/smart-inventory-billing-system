import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

def connection():
    con = psycopg2.connect(
        host="localhost",
        database="ecommerce",
        user="postgres",
        password= os.getenv("DB_PASSWORD"),
        port="5432"
    )

    print("Connection successful")

    cursor = con.cursor()

    cursor.execute("SELECT * FROM products LIMIT 5")

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    con.close()


connection()
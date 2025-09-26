import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os

# .env file read karne ke liye
load_dotenv()

try:
    conn = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )
    if conn.is_connected():
        print("✅ Connected to MySQL server!")
    conn.close()
except Error as e:
    print("❌ Error:", e)

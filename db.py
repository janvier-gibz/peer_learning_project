import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()


def connect_db():
    try:
        conn = mysql.connector.connect(
            host="mysql-database-learning-alustudent-4039.c.aivencloud.com",
            port=27289,
            user="avnadmin",
            password = os.getenv("DB_PASSWORD"),
            database="defaultdb",
            ssl_ca="ca.pem"
        )
        print("Connected to Aiven MySQL")
        return conn

    except Exception as e:
        print("Database connection failed:", e)
        return None


def create_tables(conn):
    cursor = conn.cursor()

    print("Creating tables...")

    cursor.execute("USE defaultdb")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100),
        price FLOAT,
        quantity INT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS sales (
        id INT AUTO_INCREMENT PRIMARY KEY,
        product_name VARCHAR(100),
        quantity INT,
        total_price FLOAT,
        phone VARCHAR(20),
        location VARCHAR(100)
    )
    """)

    conn.commit()
    print("Tables created successfully")
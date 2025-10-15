import mysql.connector
from mysql.connector import errorcode

def create_database():
    try:
        # Connect to MySQL server (adjust user/password/host as needed)
        conn = mysql.connector.connect(
            host="localhost",
            user="your_username",
            password="your_password"
        )
        cursor = conn.cursor()

        # Create database (using IF NOT EXISTS avoids needing SHOW/SELECT)
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        # Ensure connection is closed properly
        if 'cursor' in locals() and cursor:
            cursor.close()
        if 'conn' in locals() and conn.is_connected():
            conn.close()

if __name__ == "__main__":
    create_database()

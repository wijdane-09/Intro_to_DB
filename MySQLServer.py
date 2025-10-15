import mysql.connector
from mysql.connector import errorcode

def create_database():
    try:
        # Connect to the MySQL server (no specific database yet)
        conn = mysql.connector.connect(
            host="localhost",
            user="your_username",        # replace with your MySQL username
            password="your_password"     # replace with your MySQL password
        )
        cursor = conn.cursor()

        # Create the database if it doesn't exist
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        # Clean up and close connections
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals() and conn.is_connected():
            conn.close()

if __name__ == "__main__":
    create_database()

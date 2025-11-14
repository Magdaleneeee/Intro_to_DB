import mysql.connector
from mysql.connector import Error

try:
    # Connect to MySQL server (change user & password if needed)
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Isaiah60:1-3"        # <-- put your MySQL password here if you have one
    )
    
    if connection.is_connected():
        cursor = connection.cursor()
        
        # Create database (won't fail if exists)
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        
        print("Database 'alx_book_store' created successfully!")

except Error as e:
    print(f"Error connecting to MySQL Server: {e}")

finally:
    try:
        if connection.is_connected():
            cursor.close()
            connection.close()
    except:
        pass

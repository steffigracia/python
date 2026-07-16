import mysql.connector
from mysql.connector import Error
def get_connection():
    try:
        connection = mysql.connector.connect (
            host = "localhost",
            port = 3306,
            database = "steffi",
            user = "root",
            password = "Steffi@3108"
        )
        if connection.is_connected():
            print("Connection Established Successfully")
            return connection
    except Error as e:
        print("Error while connecting to Database",e)
        return None
def close_connection(connection,cursor = None):
    if cursor:
        cursor.close()
    if connection.is_connected():
        connection.close()
        print("Connection closed Successfully")







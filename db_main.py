from db_connection import get_connection,close_connection

def fetch_users():
    connection = get_connection()

    if connection is None:
        print("Failed to connect to Database")
        return
    cursor = None

    try:
        cursor = connection.cursor()
        query = "select * from employees"
        cursor.execute(query)
        rows = cursor.fetchall()

        for row in rows:
            print(row)
    except Exception as e:
        print("Error while running the query",e)
        return
    finally:
        close_connection(connection,cursor)

if __name__ == "__main__":
    fetch_users()


from db_connection import get_connection,close_connection

def fetch_users():
    connection = get_connection()
    if connection is None:
        print("Failed to connect to database")
        return
    cursor = None
    try:
        cursor = connection.cursor()
        query = "select * from employees"
        cursor.execute(query)
        rows = cursor.fetchall()
        #for row in rows:
            #print(row)
        return rows
    except Exception as e:
        print("Error running query",e)
    #finally:
        #connection.close(connection,cursor)

def emp_by_id(id):
    connection = get_connection()
    if connection is None:
        print("Failed to connect to database")
        return
    cursor = connection.cursor()
    cursor.execute("select * from employees where employee_id = %s",(id,))
    user = cursor.fetchone()
    #print(user)
    return user
    #close_connection(connection,cursor)

def emp(id,salary):
    connection = get_connection(dictionary = True)
    if connection is None:
        print("Failed to connect Database")
        return
    cursor = connection.cursor()
    cursor.execute("select * from employees where eemployee_id = %s and salary = %s",(id,salary))
    user = cursor.fetchone()
    print(user)
    close_connection(connection,cursor)

def multiplestudents():
    connection = get_connection()
    if connection is None:
        print("Failed to connect Database")
        return
    cursor = connection.cursor()
    names = ["bob","abdul"]
    placeholder = ",".join(["%s"]*len(names))

    query = f"select * from employees where first_name in ({placeholder})"
    cursor.execute(query,names)
    user = cursor.fetchall()
    print(user)
    close_connection(connection,cursor)
def insertdata(data):
    connection = get_connection()
    if connection is None:
        print("Failed to connect Database")
        return
    cursor = connection.cursor()
    sql = "insert into employees values (%s, %s, %s ,%s ,%s,%s)"
    #values = (6,"Steffi","Gracia",40000,98766688,"abc45@gmail.com")
    values = (data["employee_id"],data["first_name"],data["last_name"],data["salary"],data["mobile_no"],data["email"])
    cursor.execute(sql,values)
    connection.commit()
    print("Data Inserted Successfully")
    #close_connection(connection,cursor)



#if __name__ == "__main__":
    #emp_by_id(2)
    #multiplestudents()
    #insertdata()



        
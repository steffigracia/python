def login():
    username = "Steffi"
    password = "12345"
    attempt = 3
    while attempt >0:
        inputusername = input("Enter your Username: ")
        inputpassword = input("Enter your Password: ")
        if inputusername == username and inputpassword == password:
            print("Login Successful!")
            break
        else:
            print("Either username or password is incorrect")
            attempt = attempt - 1
        if attempt == 0:
            print("Limit Exceeded! Please Try Again Later.")
            break
def registration():
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    reenterpassword = input("Re-Enter Password: ")
    if reenterpassword == password:
        print("Registration Successful!")
    else:
        print("Enter the correct password")

option = int(input("Enter the operation to perform: 1.Login 2.register"))
if option == 1:
    login()
else:
    registration()

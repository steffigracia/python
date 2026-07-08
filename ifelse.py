username = "Steffi"
password = "1234"

inputusername = input("Enter your username: ")
inputpassword = input("Enter your password: ")

if(inputusername == username and inputpassword == password):
    print("Login Successful")
else:
    print("Either Username or Password is incorrect")
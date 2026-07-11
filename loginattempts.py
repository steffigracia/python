username = "Steffi"
password = "12345"
attempts = 3
while attempts > 0:
    inputusername = input("Enter your Username: ")
    inputpassword = input("Enter your Password: ")

    if inputusername == username and inputpassword == password:
        print("Login Successful")
        break
    else:
        print("Either username or password is incorrect")
        attempts-=1
       

    if attempts == 0:
        print("Limit Exceeded! Please try again")
        break
        
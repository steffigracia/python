userdata = [
    {
        "username" :"Steffi",
        "password" : "12345" 
    },
    {
        "username" : "Gracia",
        "password" : "4567"
    },
    {
        "username" : "Jabez",
        "password" : "3456"
    }

]
ispresent = False

inusername = input("Enter your username: ")
inpassword = input("Enter your password: ")
for user in userdata:
    if user["username"] == inusername and user["password"] == inpassword:
        ispresent = True
        break

if ispresent:
    print("Login Successful")
else:
    print("Either username or password is incorrect")       
    
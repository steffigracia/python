num1 = int(input("Enter first Number: "))
num2 = int(input("Enter second Number: "))

operation = int(input("Enter a operation to perform: 1.Addition 2.Subtraction 3.Multiplication 4.Division"))
if (operation == 1):
    print("Addition of", num1, "and", num2, "is: ", num1 + num2)
elif(operation == 2):
    print("Subtraction of", num1, "and", num2, "is: ", num1 - num2)
elif(operation == 3):
    print("Multiplication of", num1, "and", num2, "is: ", num1 * num2)
elif(operation == 4):
    print("Division of", num1, "and", num2, "is: ", num1 / num2)
else:
    print("Invalid Operation. Choose a valid operation from 1 to 4")
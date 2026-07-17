try:
    a = int(input("Enter a value: "))
    b = int(input("Enter b value: "))
    print("Result:",a/b)

#except ZeroDivisionError:
    #print("Cannot divide by zero")

except Exception as e:
    print("Error: ",e)

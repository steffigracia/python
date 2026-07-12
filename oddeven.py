def oddeven():
    if num % 2 == 0:
        print(f"The number {num} is even")
    else:
        print(f"The number {num} is odd")
    
        
num = int(input("Enter a number: "))
oddeven()
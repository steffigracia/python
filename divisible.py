# program to print numbers that are divisible by 5 and 7

num = int(input("Enter a Number: "))
if num%5 == 0 and num%7 ==0:
    print(f"The number {num} is divisible by 5 and 7")
elif num%5 == 0:
    print(f"The number  {num} is divible by 5 but not 7")
elif num%7 == 0:
    print(f"The number {num} is divisible by 7 but not 5")
else:
    print(f"The number {num} is not divisible by 5 and 7")
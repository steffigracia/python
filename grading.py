marks = int(input("Enter your mark: "))
if marks < 0 and marks > 100:
    print("Invalid Mark")
elif marks >= 90 and marks <=100:
    print("Grade : A+")
elif marks >= 80:
    print("Grade : A")
elif marks >= 70:
    print("Grade : B")
elif marks >= 60:
    print("Grade : C")
elif marks >= 50:
    print("Grade : D")
else:
    print("Fail")


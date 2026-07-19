import csv

with open("employees.csv","r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        if row[3] == "Full stack":
            print(row)
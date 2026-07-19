import csv

with open("employees.csv","w",newline = "") as file:
    fieldname = ["ID","Name","Salary","Department"]
    writer = csv.DictWriter(file,fieldnames = fieldname)
    writer.writeheader()
    writer.writerow({
        "ID" : 1,
        "Name" : "Steffi",
        "Salary" : 50000,
        "Department" : "Developer"
    })
    
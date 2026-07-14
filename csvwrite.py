import csv
with open ("emp.csv","w",newline = "") as file:
    writer = csv.writer(file)
    writer.writerow(["ID","Name","Salary"])
    writer.writerow([1,"Steffi",50000])
    writer.writerow([2,"Gracia",60000])
    writer.writerow([3,"Jabez",60000])
    writer.writerow([4,"Sugi",70000])
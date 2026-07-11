student = {
    "s.no" : 1,
    "Name" : "Steffi",
    "Age" : 21,
    "Grade" : 'A'
}
print(student)

StudentN = dict(name = "Gracia", age = 20)
print(StudentN)

print(student.get("Name"))

student["City"] = "Madurai"
print(student)

print(student.get("City"))

student["State"] = "Tamilnadu"
print(student)

del student["State"]
print(student)

student.pop("Grade")
print(student)

#print(student.clear()) # clear elements in the dictionary
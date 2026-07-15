lines = ["Java\n","Python\n","RestAPI"]

with open ("sample.txt","a") as file:
    file.write("\n Append Operation")
    file.writelines(lines)

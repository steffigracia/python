t = (123,456,234,345,567,678,789)
print("Tuple: ",t)
#print tuple using forloop
for n in t:
    print(n)

#Appending elements to tuple
#convert tuple to list
lst = list(t)
lst.append(890)
print(lst)
#convert list to tuple
t = tuple(lst)
print(t)
s = set()

s = {1,2,3,4,5,2}
print(s)

s.add(6)
print(s)

s.remove(3)
print(s)

print(len(s))

s2 = s.copy()
print(s2)

print(s.union(s2))
s2.add(7)
print(s2)

print(s.intersection(s2))
print(s.difference(s2))

print(s2.difference(s))
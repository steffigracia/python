class comments:
    id = 0
    body = ""
    postid = 0
    likes = 0

c = comments()
c.id = 1
c.body = "abcdefg"
c.postid = 1
c.likes = 100
print(c.id)
print(c.likes)

c2 = comments()
c2.id = 2
c2.body = "hijklm"
c2.postid = 2
c2.likes = 200
print(c2.postid)
print(c2.likes)

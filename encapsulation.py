class Student:
    def __init__(self,name,marks):
        self.name = name
        self.__marks = marks
    def get_marks(self):
        return self.__marks
    def set_marks(self,marks):
        if marks>=0 and marks<=100:
            self.__marks = marks
        else:
            print("Invalid Marks")
s = Student("Anu",85)
print("Name: ",s.name)
print("Marks: ",s.get_marks())
s.set_marks(95)
print("Updated Mark: ",s.get_marks())
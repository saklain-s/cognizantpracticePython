class Student:

    def __init__(self,name,marks):
        self.name = name
        self.__marks = marks

    def get_marks(self):
        return self.__marks

    def set_marks(self,value):
        if 0 <= value <= 100:
            self.__marks = value
        else:
            print("Invalid marks! Must be between 0 to 100")


s1 = Student("Saklain",85)

print(s1.get_marks())

s1.set_marks(99)

print(s1.get_marks())

print(s1._Student__marks) # mangling

# e
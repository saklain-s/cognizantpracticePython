class Person:
    def __init__(self,name):
        self.name = name

    def greet(self):
        print(f"Hello, my name is {self.name}")

class Student(Person):

    def study(self):
        print(f"{self.name} is studying")

s1 = Student("Saklain")
s1.greet()
s1.study()
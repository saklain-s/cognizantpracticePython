# Sometimes, you want to extend parent functionality — not completely replace it.
# That’s where super() helps.

class Person:
    def __init__(self,name):
        self.name = name

class Student(Person):
    def __init__(self,name,roll):
        super().__init__(name)
        self.roll = roll

    def display(self):
        print(f"Name: {self.name}, Roll:{self.roll}")

s1 = Student("saklain",97)
s1.display()
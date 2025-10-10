class Student:
    school = "Raghu College"  # class variable

    def __init__(self, name):
        self.name = name      # instance variable

s1 = Student("Saklain")
s2 = Student("Rahul")

print(s1.school)  # Raghu College
print(s2.school)  # Raghu College
print(s1.name)    # Saklain
print(s2.name)    # Rahul

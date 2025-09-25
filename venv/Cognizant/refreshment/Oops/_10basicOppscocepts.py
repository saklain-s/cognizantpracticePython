# class student:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     def display(self):
#         print(f"Name: {self.name} Age: {self.age}")
#
#
# s = student("saklain",23)
# s.display()
from tkinter.font import names


# class Student:
#     college = "ABC university"
#
#     def __init__(self,name):
#         self.name = name
#
# s1 = Student("Saklain")
# s2 = Student("Rahul")
#
# print(s1.name,s1.college)
# print(s2.name,s2.college)

#Types of methods

class Demo:
    def instance_method(self):
        print("Instance method") #need self

    @classmethod
    def class_method(cls):  #need class
        print("Class Method")

    @staticmethod
    def static_method(): #no self, no cls
        print("Static method")

Obf = Demo()

Obf.instance_method()

Demo.class_method()
Demo.static_method()
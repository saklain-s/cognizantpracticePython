class Grandparent:
    def func1(self):
        print("Grand parent")

class Parent(Grandparent):
    def func2(self):
        print("Parent")

class Child(Parent):
    def func3(self):
        print("Child")

obj = Child()
obj.func1()
obj.func2()
obj.func3()


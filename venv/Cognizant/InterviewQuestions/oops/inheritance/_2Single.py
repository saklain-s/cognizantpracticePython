class Parent:
    def func1(self):
        print("Parent class method")

class Child(Parent):
    def func2(self):
        print("Child class method")

obg = Child()
obg.func1()
obg.func2()
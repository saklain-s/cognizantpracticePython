class Father:
    def func1(self):
        print("Father's Method")

class Mother:
    def func2(self):
        print("Mother's Method")

class Child(Father,Mother):
    def func3(self):
        print("Child's Method")

c = Child()
c.func1()
c.func2()
c.func3()
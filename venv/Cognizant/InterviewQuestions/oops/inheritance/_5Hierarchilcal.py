class Parent:
    def show(self):
        print("Parent Method")

class Child1(Parent):
    def child1(self):
        print("Child1 method")

class Child2(Parent):
    def child2(self):
        print("Child2 method")

c1 = Child1()
c2 = Child2()

c1.show()
c2.show()
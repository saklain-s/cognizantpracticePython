class A:
    def funcA(self):
        print("Class A")

class B(A):
    def funcB(self):
        print("Class B")

class C(A):
    def funcC(self):
        print("Class C")

class D(B, C):
    def funcD(self):
        print("Class D")

obj = D()
obj.funcA()
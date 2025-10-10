class Demo:
    class_var = 10

    def instance_method(self):
        print("Called instance method", self.class_var)

    @classmethod
    def class_method(cls):
        print("Called class method", cls.class_var)

    @staticmethod
    def static_method():
        print("Called static method")

obj = Demo()
obj.instance_method()  # Called instance method 10
Demo.class_method()    # Called class method 10
Demo.static_method()   # Called static method

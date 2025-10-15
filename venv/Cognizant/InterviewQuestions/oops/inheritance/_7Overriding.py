class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):  # overriding parent method
        print("Dog barks")

obj = Dog()
obj.sound()

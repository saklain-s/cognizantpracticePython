class Animal:
    @classmethod
    def eat(self):
        print("Animals make sound")

class Dog(Animal):
    @classmethod
    def speak(self):
        super().eat() # to call class animals methods without creating any objects
        print("Dog barks")

d = Dog()
# a = Animal()

Dog.speak()
print()
Dog.eat()
print()
d.speak()
print()
d.eat()


class person:
    def greet(self):
        print("Hello from person")

class student(person):
    def greet(self):
        super().greet()
        print("Hello from student")

s = student()
s.greet()
class Dog:
    def sound(self):
        print("Dog barks")

class Cat:
    def sound(self):
        print("Cat mewos")


for animal in[Dog(), Cat()]:
    animal.sound()
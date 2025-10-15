# ----- Parent Class -----
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Some generic animal sound"

# ----- Child Classes -----
class Dog(Animal):   # Inherits from Animal
    def speak(self):
        return "Woof!"

class Cat(Animal):   # Inherits from Animal
    def speak(self):
        return "Meow!"

class Cow(Animal):   # Inherits from Animal
    def speak(self):
        return "Moo!"

# ----- Polymorphism in action -----
animals = [Dog("Bruno"), Cat("Kitty"), Cow("Ganga")]

for animal in animals:
    print(f"{animal.name} says: {animal.speak()}")

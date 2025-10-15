class Bird:
    def fly(self):
        print("Bird is flying")

class Sparrow(Bird):
    def fly(self):
        print("Sparrow is at low height")

class Eagle(Bird):
    def fly(self):
        print("Eagle flies at high height")


for bird in [Bird(),Sparrow(),Eagle()]:
    bird.fly()
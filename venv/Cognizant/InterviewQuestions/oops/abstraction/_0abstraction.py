
from abc import ABC, abstractmethod

#abstact base class
class vehicle(ABC):

    @abstractmethod
    def start(self):
        """“Do nothing here — just move on.”

Python doesn’t allow empty code blocks,
so whenever you want to define something syntactically but don’t have logic yet, you use pass."""
        pass

    @abstractmethod
    def stop(self):
        pass

# concrete class implementing abstract methods
class Car(vehicle):
    def start(self):
        print("Car Engine Started")

    def stop(self):
        print("Car engine stopped")

class Bike(vehicle):
    def start(self):
        print("Bike engine started")

    def stop(self):
        print("Bike Engine stopped")


car = Car()
car.start()
car.stop()

bike = Bike()
bike.start()
bike.stop()

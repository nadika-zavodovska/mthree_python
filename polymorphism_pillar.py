from abc import ABC, abstractmethod

class Pet(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Pet):
    def speak(self):
        print("Bark, Woof")

class Cat(Pet):
    def speak(self):
        print("Meow!")

class Rabbit(Pet):
    def speak(self):
        print("Some sound!")

# declare a function which takes a reference variable

def accept(pet):
    pet.speak()

accept(Dog())
accept(Cat())
accept(Rabbit())

# Duck Typing

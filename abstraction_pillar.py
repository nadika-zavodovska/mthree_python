from abc import ABC, abstractmethod

class A(ABC):
    @abstractmethod  # This is one of the decorators
    def get_a(self):
        pass

class B(A):
    def get_a(self):  # This method override method in class A
        print("This is get_a method")

# a1 = A()

b1 = B()
b1.get_a()

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

# p1 = Pet()  # Can't instantiate abstract class

d1 = Dog()
d1.speak()

c1 = Cat()
c1.speak()

r1 = Rabbit()
r1.speak()

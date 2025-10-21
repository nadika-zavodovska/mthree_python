# Step #1 Create a class
class Animal:
    def __init__(self, id, size, color, age, weight):
        self.id = id        
        self.size = size
        self.color = color
        self.age = age
        self.weight = weight
        
    """@property lets you define a method that can be accessed 
    like an attribute, giving you the simplicity of a variable
    with the power of a function
    """
    @property
    def species(self):
        return self.__class__.__name__

    def getAnimalDetails(self):
        return f"ID: {self.id}, Size: {self.size}, Colour: {self.color}, Age: {self.age}, Weight: {self.weight}"

"""
Inheritance. Cat, Dog, and Rabbit classes inherit from Animal class (state __init__(id, size, color etc), species property, getAnimalDetails())
Each subclass adds/overrides what is specific to the animal
"""
class Cat(Animal):
    def getAnimalLifespan(self):
        return "13 - 20 years"
    def getAnimalMaxspeed(self):
        return "40 km/h"

class Dog(Animal):
    def getAnimalLifespan(self):
        return "10 - 15 years"
    def getAnimalMaxspeed(self):
        return "45 km/h"

class Rabbit(Animal):
    def getAnimalLifespan(self):
        return "7 - 9 years"
    def getAnimalMaxspeed(self):
        return "40 km/h"

# Step #2 Create objects using subclasses(children classes)
cat = Cat(1, "small", "white", 2, "3 kg")
dog = Dog(2, "large", "black", 7, "30 kg")
rabbit = Rabbit(3, "small", "brown", 10, "2.5 kg")

# Step #3 Group classes in a list
list_animals = [cat, dog, rabbit]

""" 
Example of polymorphism pillar 
Polymorphism - same code calling the same method name on different objects, and each object responds in its own way.
"""
# Step  # 4 Display values of the objects through list iteration
for animal in list_animals:
    print(f"* {type(animal).__name__} *")
    print(animal.getAnimalDetails())
    print(f"Lifespan: {animal.getAnimalLifespan()}")

# Step #1 Create a class
class Animal:
    def __init__(self, id, species, size, colour, age, weight):
        self.id = id
        self.species = species
        self.size = size
        self.colour = colour
        self.age = age
        self.weight = weight

    def getAnimalDetails(self):
        return f"ID: {self.id}, Type: {self.species}, Size: {self.size}, Colour: {self.colour}, Age: {self.age}, Weight: {self.weight}"

    def getAnimalLifespan(self):
        if self.species.lower() == "cat":
            return "13 - 20 years"
        elif self.species.lower() == "dog":
            return "10 - 15 years"
        elif self.species.lower() == "lion":
            return "12 - 17 years"
    
    def getAnimalMaxspeed(self):
        if self.species.lower() == "cat":
            return "40 km/h"
        elif self.species.lower() == "dog":
            return "45 km/h"
        elif self.species.lower() == "lion":
            return "80 km/h"

# Step #2 Create objects from Class
cat = Animal(1, "Cat", "small", "white", 2, "3 kg")
dog = Animal(2, "Dog", "large", "black", 7, "30 kg")
lion = Animal(3, "Lion", "large", "brown", 10, "150 kg")

# Step #3 Group objects in a list
list_animals = [cat, dog, lion]

# Step #4 Display values of the objects through list iterating 
for animal in list_animals:
    print(animal.getAnimalDetails())
    
for animal in list_animals:
    print(f"Lifespan: {animal.species} - {animal.getAnimalLifespan()}")
    
for animal in list_animals:
    print(f"Max speed: {animal.species} - {animal.getAnimalMaxspeed()}")

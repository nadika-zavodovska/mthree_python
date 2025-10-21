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

# Step #2 Create objects from the Class
cat = Animal(1, "Cat", "small", "white", 2, "3 kg")
dog = Animal(2, "Dog", "large", "black", 7, "30 kg")
lion = Animal(3, "Lion", "large", "brown", 10, "150 kg")

# Step #3 Group objects in a list
list_animals = [cat, dog, lion]

# Step #4 Display values of the objects through list iteration
for animal in list_animals:
    print(animal.getAnimalDetails())

for animal in list_animals:
    print(f"Lifespan: {animal.species} - {animal.getAnimalLifespan()}")

for animal in list_animals:
    print(f"Max speed: {animal.species} - {animal.getAnimalMaxspeed()}")


# Add Owner class
class Owner:
    def __init__(self, name, contact):
        self.name = name
        self.contact = contact
        self.animals = []

    def add(self, animal):
        self.animals.append(animal)

    def remove(self, name):
        # Store animals we want to keep
        new_list = []
        for animal in self.animals:
            if animal.name != name:
                new_list.append(animal)
        self.animals = new_list

    def list(self):
        return self.animals

# Craete an object (Owner is a parent)
owner_1 = Owner("Tom", "07348370947")

owner_1.add(cat)
owner_1.add(dog)

print(f"{owner_1.name} has animals: ")

for animal in owner_1.animals:
    print(animal.getAnimalDetails())

class Pet:
    def __init__(self, pet_name, pet_color):
        self.pet_name = pet_name
        self.pet_color = pet_color

    def getPetDetails(self):
        return f"Pet Name : {self.pet_name}, Pet Color : {self.pet_color}"

# Step 1
class Employee:
    def __init__(self, id, name, salary, pets):
        self.id = id
        self.name = name
        self.salary = salary
        self.pets = (
            pets  # This line builds has-a relationship between Employee and Pet class
        )

    def getEmployeeDetails(self):
        return f"ID : {self.id}, NAME : {self.name}, SALARY : {self.salary}"


pet1 = Pet("A", "White")
pet2 = Pet("B", "Black")
pet3 = Pet("C", "White")

pets = [pet1, pet2, pet3]

e1 = Employee(
    1, "Alex", 3000, pets
)  # This line invokes __init__ written in Employee class automatically

print(e1.getEmployeeDetails())
print("*********************")
for pet in e1.pets:
    print(pet.getPetDetails())

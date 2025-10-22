# Task:
# Write a lambda for map function which takes employee object as an input and returns employee name?

# Solution
class Employee:
    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary

    def getEmployeeDetails(self):
        return f"ID : {self.id}, NAME : {self.name}, SALARY : {self.salary}"

# Create objects
employee_1 = Employee(1, "Alex", 3000)
employee_2 = Employee(2, "Chris", 4000)
employee_3 = Employee(3, "Maria", 3500)
employee_4 = Employee(4, "Oliver", 5000)

# Add objects to a list
list_employees = [employee_1, employee_2, employee_3, employee_4]
# Map using lambda function
employee_names = list(map(lambda employee: employee.name, list_employees))

print("Names of employees:")
for name in employee_names:
    print(name)

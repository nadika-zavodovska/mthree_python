# Step 1
class Employee:
    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary

    def getEmployeeDetails(self):
        return f"ID : {self.id}, NAME : {self.name}, SALARY : {self.salary}"

    @staticmethod
    def validate_id(id):
        if id < 0:
            return False
        else:
            return True


# Please review PEP 8 Style Guide
class Manager(Employee):
    def __init__(self, id, name, salary, dept_name):
        super().__init__(id, name, salary)
        self.dept_name = dept_name

    def getManagerDetails(self):
        return f"{super().getEmployeeDetails()}, DEPT NAME : {self.dept_name}"


id = int(input("Enter any ID"))

valid = Employee.validate_id(id)

if valid:
    e1 = Employee(id, "Alex", 3000)

mgr1 = Manager(2, "Tom", 5000, "IT")

print(e1.getEmployeeDetails())

print(mgr1.getManagerDetails())

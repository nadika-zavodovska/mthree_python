class Employee:
    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary

    @classmethod
    def create_emp_object(cls, id, name, salary):
        return cls(id, name, salary)

    def display(self):
        print("Hello")


# Employee.display()

x = Employee(2, "Bob", 4000)

e1 = Employee.create_emp_object(1, "Alex", 3000)

e1.display()
print(e1.name)

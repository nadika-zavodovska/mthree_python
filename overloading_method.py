from multipledispatch import dispatch

class Calculator:
    @dispatch(int, int, int)
    def add(self, x, y, z):
        return x + y + z

    @dispatch(int, int)
    def add(self, x, y):
        return x + y

calc = Calculator()

print(calc.add(100, 200))
print(calc.add(100, 200, 300))

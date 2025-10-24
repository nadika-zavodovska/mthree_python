a = int(input("Enter value for a"))
b = int(input("Enter value for b"))

try:
    print(a / b)
except ZeroDivisionError as e:
    print(f"Division Error {e}")
finally:
    print("From finally block")

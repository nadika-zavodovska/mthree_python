try:
    print(10 / 0)
except ZeroDivisionError as e:
    print(f"An exception occured {e}")

#  print("Continue...")

try:
    x = int(input("Enter a number: "))
except ValueError as e:
    print(f"Type is not correct {e}")

# Prevent division by zero
# If user enters 0, print "Can't divide by zero"

try:
    num = int(input("Enter divisor: "))
    result = 100 / num
    print(result)
except ZeroDivisionError as e:
    print(f"Can't divide by zero {e}")

# Try adding a string and number.
# If TypeError occurs, print "Type mismatch".

try:
    result = 10 + "5"
    print(result)
except TypeError as e:
    print(f"Type error: cannot add number and string {e}")

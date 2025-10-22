# Activity 1

"""
Create a computer program that performs the following steps:

Prompt the user for an integer and store the value in a variable.
Display the data type of the variable that holds the entered data.
Convert the value to an integer type and store the converted value in a new variable.
Display the value and type of the new variable in a single sentence. (For example, "The value is 8 with type integer.")
Run the program and enter a float value at the prompt. What is its value in the last step?
Refactor the program, using a float instead of an integer. What happens if you enter an integer rather than a float at the prompt?
"""

""" 
Solution
This line returns a string
"""
user_number = input("Enter a number: ")
print(type(user_number))
# Convert string to float
number = float(user_number)
# convert to integer (drops decimal part)
converted_integer = int(number)
print(f"The value is {converted_integer} with type {type(converted_integer)}.")

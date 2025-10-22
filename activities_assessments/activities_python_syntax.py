# Activity 1

# Task #1
# display the text in quotation marks to an output block
# Print("Python is fun!")

"""" Fixed code
We use lowercase for functions. Python is case-sensitive language.
"""
print("Python is fun!")

# ***

# Task #2
# Display the text in quotation marks to an output block
# without moving any of the existing acode to a different line
# print("Python is fun!") print("Python is also easy.")

""" Fixed code
I added ; to make possible write multiple lines on one line
"""
print("Python is fun!"); print("Python is also easy.")

# ***

# Task #3
# Display the text in quotation marks to an output block
# without moving any of the existing code to a different line
print
("Python is fun!")

""" Fixed code
I added \ . It treats next line as it is a part of the same line
"""
print \
("Python is fun!")

# ***

# Task #4
# Change each variable name to an appropriate name for Python.
# Do not use the same variable name more than one time.
# 1-name = "Rebecca" # first name
# &_name = "Roberts" # last name

# After changing the variable names, update the code below
# to print out each name.
# print(1-name)
# print(&_name)

"""Fixed code:
There is a rule - we can't start variable names with a number or symbol"""
first_name = "Rebecca" # first name
last_name = "Roberts" # last name

print(first_name)
print(last_name)

# ***

# Activity 2

# Add a new line of code that displays the text in quotation marks
# to an output block without repeating the text in quotation marks.
output = "I love Python!"

# your code below this line

"""Fixed code:
I used output variable to print the string 
"""
print(output)

# ***

# Activity 3

# Create a script that prompts the user for the name of the state where they were born and the name of the state where they live now. Save each value in its own variable and display the input values to the user.

"""Fixed code
I used input function to promt user for the name of the state 
"""
user_born_state = input("Where were you born? ")
user_live_state = input("Where do you live now? ")

print(f"You were born in {user_born_state}.")
print(f"You are living in {user_live_state} now.")

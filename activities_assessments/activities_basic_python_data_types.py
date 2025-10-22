import math

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

# Solution

# This line returns a string
# user_number = input("Enter a number: ")
# print(type(user_number))
# # Convert string to float
# number = float(user_number)
# # convert to integer (drops decimal part)
# converted_integer = int(number)
# print(f"The value is {converted_integer} with type {type(converted_integer)}.")

# ***

"""
Activity 2
Update the code below so that the result is equal to 576.
Do not change any of the existing values or operators or the order in which they appear.
"""

# do not change the order in which the numbers and operators appear in the next line
# result = 5 + 3**2 * 9

# print(result)  # the output should be 576

# Solution:
# I added parentheses to change the order of evaluation
# result = (5 + 3) ** 2 * 9

# print(result)

# ***

""" Activity 3
Create a computer program that prompts the user for a float number and returns the integer portion of the floating number.
"""

# Solution

# def convert_float_int():
#     user_float_num = input("Enter a float number ")
#     converted_float = float(user_float_num)
#     return int(converted_float)

# user_int_num = convert_float_int()
# print(f"Your integer number is {user_int_num}")

# ***

"""
Activity 4
Write a computer program that calculates and displays the current value of a deposit for a given initial deposit, interest rate, how many times interest is calculated per year, and the number of years since the initial deposit.

The program should prompt the user for each of the values and use the following formula to calculate the current value of the deposit:

V = P(1 + r/n)^nt
where

V -- value
P -- initial deposit
r -- interest rate as a fraction (eg 0.05)
n -- the number of times per year interest is calculated
t -- the number of years since the initial deposit
The program should display each of the values entered to the user in a meaningful way (so that the user can easily see what each value represents), along with the results of the calculation.
"""

# def get_user_value_deposit():
#     user_initial_deposit = float(input("What is your initial deposit? "))
#     user_fraction_interest_rate = float(input("What is your interest rate as a fraction? "))
#     user_num_times_calcul_deposit_year = int(input("How many numbers of times per year interest is calculated?"))
#     user_years_deposit = float(input("How many numbers of year since the initial deposit?"))

#     value_deposit = user_initial_deposit * (
#         1 + user_fraction_interest_rate / user_num_times_calcul_deposit_year
#     ) ** (user_num_times_calcul_deposit_year * user_years_deposit)
#     round_value_deposit = round(value_deposit, 2)

#     # Return tuple with 5 values
#     return (
#         round_value_deposit,
#         user_initial_deposit,
#         user_fraction_interest_rate,
#         user_num_times_calcul_deposit_year,
#         user_years_deposit,
#     )

# # Unpack tuples
# (
#     user_value_deposit,
#     user_initial_deposit,
#     user_fraction_interest_rate,
#     user_num_times_calcul_deposit_year,
#     user_years_deposit,
# ) = get_user_value_deposit()

# print(
#     f"""========
# Your bank details:
# Your current value of your deposit is £{user_value_deposit}.
# Your initial deposit is £{user_initial_deposit}.
# Your interest rate is {user_fraction_interest_rate * 100:.2f}%.
# Your interest is calculated {user_num_times_calcul_deposit_year} times per year.
# {user_years_deposit} years since your initial deposit.
# """
# )

# ***

# Activity 5
"""
Write a computer program that prompts the user for a principal amount, the rate of interest, and the number of days for a loan and then calculates and returns the simple interest for the life of the loan. Use the formula:
interest = principal * rate * days / 365
"""

# Solution:

# def get_interest_for_loan():
#     principal_amount = float(input("Enter principal amount: "))
#     interest_rate = float(input("Enter your interest rate "))
#     days_loan = int(input("Enter number of days for the loan: "))

#     interest = principal_amount * interest_rate * days_loan / 365

#     return interest

# interest_value = get_interest_for_loan()

# print(f"The simple interest for the life of the loan is {interest_value:.2f}")

# Activity 6
"""
Create a computer program that displays three statements that evaluate to True and three statements that evaluate to False.
Example:
a = 0
b = 1 

Output: a < b = True
"""

# Solution:
# a = 0
# b = 1

# print("---True statements---")
# print(a < b)
# print(b > a)
# print(a != b)

# print("---False statements---")
# print(a == b)
# print(a > b)
# print(b < a)

# ***

# Activity 7
"""
Create a computer program that prompts the user for a number and calculates the following:

the boolean of the number entered
the binary equivalent of the number entered
the square root of the number entered
The program should display the following to the user:

The number the user entered, in a phrase like, "You selected value."
The boolean of the number, in a phrase like, "The boolean of your number is value."
The binary equivalent of the number, in a phrase like, "The binary equivalent of your number is value"
The square root of the number, in a phrase like, "The square root of your number is value," with the value rounded to three decimal places.
"""

# Solution

user_number = int(float(input("Enter a number - ")))

user_number_boolean = bool(user_number)
user_number_binary = bin(user_number)
user_number_sqrt = math.sqrt(user_number)

print(
    f"""
      You selected {user_number}.
      The boolean of your number is {user_number_boolean}.
      The binary equivalent of your number is {user_number_binary}
      The square root of your number is {user_number_sqrt:.3f}.
      """
)

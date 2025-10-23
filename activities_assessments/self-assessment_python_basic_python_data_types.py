# Nadika Welch 23.10.2025

first_name = input("Enter your first name: ").strip().capitalize()
last_name = input("Enter your last name: ").strip().capitalize()
city = input("Enter the city where you live: ").strip().capitalize()
hourly_wage = float(input("Enter your hourly wage: "))
working_hours_per_week = float(input("Enter number of hours you work per week: "))

wage_per_week = hourly_wage * working_hours_per_week
wage_per_month = wage_per_week * 4 
wage_per_year = wage_per_week * 52

print("***********************************")
print(f"Your name: {first_name} {last_name}")
print(f"Your city: {city}")
print(f"Your weekly wage: £{wage_per_week:,.2f}")
print(f"Your monthly wage: £{wage_per_month:,.2f}")
print(f"Your yearly wage: £{wage_per_year:,.2f}")

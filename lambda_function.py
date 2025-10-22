from functools import reduce

def add(x, y):
	    return x + y

# Lambda representation of the above function
sum = lambda x, y : x + y
print(sum(10,20))

# Write new code using lambda and filter function
# filter(function,iterable/collection)

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_nums = list(filter(lambda n: n % 2 == 0, nums))

# Map and lambda function
cities = ["london", "manchester", "new york", "dublin"]
cities_in_upper_case = list(map(lambda city: city.upper(), cities))
print(cities_in_upper_case)

cities = ["london", "manchester", "new york", "dublin"]
filter_cities = list(filter(lambda city: len(city) == 6, cities))
cities_in_upper_case = list(map(lambda city: city.upper(), filter_cities))
print(cities_in_upper_case)

cities = ["london", "manchester", "new york", "dublin"]
cities_in_upper_case = list(
    map(lambda city: city.upper(), list(filter(lambda city: len(city) == 6, cities)))
)
print(cities_in_upper_case)

# Reduce and lambda
# Imperative:

nums = [1, 2, 3, 4, 5]
total = 0
for n in nums:
    total += n

print(total)

# Declarative code using reduce function
# nums = [1, 2, 3, 4, 5]
# total = reduce(lambda x, y, z: x + y + z, nums)
# print(total)


def my_func(x, y):
    return x + y

nums = [1, 2, 3, 4, 5]
total = reduce(my_func, nums)
print(total)

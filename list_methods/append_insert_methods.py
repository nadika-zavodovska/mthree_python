# Append "Paris" and "Madrid" one by one
cities = ["London", "Munich"]

cities.append("Paris")
cities.append("Madrid")
print(cities)

# *****

# Insert 30 at index 2

nums = [10, 20, 40]

nums.insert(2, 30)

print(nums)

# ****

# Use insert() not append to add "d" at the end
letters = ["a", "b", "c"]

letters.insert(len(letters), "d")
print(letters)

# ****
# Insert "banana" between apple and orange
fruits = ["apple", "orange", "mango"]

fruits.insert(1, "banana")
print(fruits)

# ****
# Using a loop and only append(), add numbers 1 to 5.
nums = []

for num in range(1, 6):
    nums.append(num)
    
print(nums)

# ****
# Using a loop and only insert(0, x), add numbers 1 to 5
nums = []

for num in range(1,6):
    nums.insert(0, num)
    
print(nums)

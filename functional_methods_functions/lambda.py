# Add two numbers

add = lambda a, b: a + b

print(add(10, 3))

# Check if a number is even

is_even = lambda num: num % 2 == 0

print(is_even(2))
print(is_even(3))

# Sort this list of tuples by the second element

pairs = [(1, 4), (3, 1), (5, 2), (4, 0)]

sorted_pairs = sorted(pairs, key = lambda nums: nums[1])
print(sorted_pairs)

# Fill the lambda to sort strings alphabetically by last letter
words = ["banana", "apple", "kiwi", "grape"]

result = sorted(words, key = lambda word: word[-1])
print(result)

# Filter even numbers using filter + lambda
nums = [1, 2, 3, 4, 5, 6]

even_nums = list(filter(lambda num: num % 2 == 0, nums))

print(even_nums)

# sum of even numbers
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
is_even = list(filter(lambda num: num % 2 == 0, nums))
sum_even_nums = sum(is_even)

print(sum_even_nums)

# Filter odd numbers
# Input: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

odd_nums = list(filter(lambda num: num % 2 != 0, nums))

print(odd_nums)

# Filter numbers greater than 50
# Input: [10, 55, 60, 22, 75, 43]
# Output: [55, 60, 75]

nums = [10, 55, 60, 22, 75, 43]

greater_50_nums = list(filter(lambda num: num > 50, nums))

print(greater_50_nums)

# Filter strings that start with "a" or "A"
# Input: ["apple", "Banana", "Avocado", "grape", "Apricot"]
# Output: ["apple", "Avocado", "Apricot"]

fruits = ["apple", "Banana", "Avocado", "grape", "Apricot"]

fruits_start_a = list(filter(lambda fruit: fruit[0].lower() == "a", fruits))

print(fruits_start_a)

# Filter only positive numbers
# Input: [-5, 3, -1, 8, 0, -2, 6]
# Output: [3, 8, 6]

nums = [-5, 3, -1, 8, 0, -2, 6]
posit_nums = list(filter(lambda num: num > 0, nums))

print(posit_nums)

# Filter words longer than 4 characters
# Input: ["cat", "elephant", "dog", "tiger", "lion"]
# Output: ["elephant", "tiger"]

animals = ["cat", "elephant", "dog", "tiger", "lion"]

longer_4_char_animals = list(filter(lambda animal: len(animal) > 4, animals))

print(longer_4_char_animals)

# Filter names that contain the letter "a"
# Input: ["Ram", "Syed", "Ali", "John", "Zain"]
# Output: ["Ram", "Ali", "Zain"]

# with magic method
names = ["Ram", "Syed", "Ali", "John", "Zain"]
names_with_a = list(filter(lambda name: name.lower().__contains__("a"), names))
print(names_with_a)

# with in
names = ["Ram", "Syed", "Ali", "John", "Zain"]
names_with_a = list(filter(lambda name: "a" in name.lower(), names))

print(names_with_a)

# Filter students who passed (marks ≥ 50)
# Input: students = [45, 89, 32, 78, 50, 99, 41]
# Output: [89, 78, 50, 99]

students = [45, 89, 32, 78, 50, 99, 41]

students_marks_more_50 = list(filter(lambda mark: mark >= 50, students))

print(students_marks_more_50)

# Filter dictionary list by key value
# Keep only students aged ≥ 18:
# people = [
#   {"name": "Ali", "age": 17},
#   {"name": "Sara", "age": 20},
#   {"name": "Tom", "age": 15},
#   {"name": "Lina", "age": 19},
# ]
# Output: [{"name": "Sara", "age": 20}, {"name": "Lina", "age": 19}]

people = [
  {"name": "Ali", "age": 17},
  {"name": "Sara", "age": 20},
  {"name": "Tom", "age": 15},
  {"name": "Lina", "age": 19},
  {"name": "Jessy", "age": 18},
]

people_older_18 = list(filter(lambda person: person["age"] >= 18, people))

print(people_older_18)

# Filter palindromes
# Input: ["level", "hello", "radar", "world", "madam"]
# Output: ["level", "radar", "madam"]

words = ["level", "hello", "radar", "world", "madam"]
polindrom_words = list(filter(lambda word: word == word[::-1], words))
print(polindrom_words)

# Filter emails that end with @gmail.com
# Input: emails = ["ali@gmail.com", "test@yahoo.com", "user@gmail.com", "abc@outlook.com"]
# Output: ["ali@gmail.com", "user@gmail.com"]

emails = ["ali@gmail.com", "test@yahoo.com", "user@gmail.com", "abc@outlook.com"]

emails_end_gmail_com = list(
    filter(lambda email: email.lower().endswith("@gmail.com"), emails)
)

print(emails_end_gmail_com)


# Filter method

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

# Map method

# Square each number

nums = [1, 2, 3, 4, 5]
square_nums = list(map(lambda num: num*2, nums))
print(square_nums)

# Convert each number to string

# Input: [1, 5, 10]
# Output: ["1", "5", "10"]

nums = [1, 5, 10]
str_nums = list(map(lambda num: str(num), nums))
print(str_nums)

# Add 10 to each number
# Input: [5, 12, 20]
# Output: [15, 22, 30]

nums = [5, 12, 20]
nums_plus_10 = list(map(lambda num: num + 10, nums))
print(nums_plus_10)

# Take length of each word
# Input: ["apple", "banana", "kiwi"]
# Output: [5, 6, 4]

fruits = ["apple", "banana", "kiwi"]
fruits_length = list(map(lambda fruit: len(fruit), fruits))
print(fruits_length)

# Convert all words to uppercase
# Input: ["hello", "world"]
# Output: ["HELLO", "WORLD"]

words = ["hello", "world"]
words_upper = list(map(lambda word: word.upper(), words))
print(words_upper)

# Convert list of floats to integers
# Input: [1.2, 5.7, 3.3]
# Output: [1, 5, 3]

float_nums = [1.2, 5.7, 3.3]
int_nums = list(map(lambda num: int(num), float_nums))
print(int_nums)

# Map two lists element-wise (sum)
# Input: List1: [1,2,3]
# List2: [4,5,6]
# Output: [5,7,9]

num_1 = [1, 2, 3]
num_2 = [4, 5, 6]
sum_nums = list(map(lambda x, y: x + y, num_1, num_2))
print(sum_nums)

# Multiply each number by its index
# Input: [10,20,30,40]
# Output: [0,20,60,120]

nums = [10, 20, 30, 40]
nums_mult_index = list(map(lambda num, index: num * index, nums, range(len(nums))))
print(nums_mult_index)

# Convert temperatures from Celsius ➜ Fahrenheit
# Formula: F = C * 9/5 + 32
# Input: [0, 10, 30, 100]
# Output: [32, 50, 86, 212]

celsius_temp = [0, 10, 30, 100]
fahrenheit_temp = list(map(lambda temp: temp * 9/5 + 32, celsius_temp))
print(fahrenheit_temp)

# Format numbers with text
# Input: [1,2,3]
# Output: ["Value: 1", "Value: 2", "Value: 3"]

nums = [1, 2, 3]
nums_text = list(map(lambda num: f"Value {num}", nums))
print(nums_text)

# Extract first char of each word
# Input: ["apple", "ball", "cat"]
# Output: ["a","b","c"]

words = ["apple", "ball", "cat"]
first_char_words = list(map(lambda word: word[0], words))
print(first_char_words)

# Convert dictionary list to only names
# Input: users = [
#   {"name": "Ali", "age": 20},
#   {"name": "Sara", "age": 22},
#   {"name": "Tom", "age": 19}
# ]
# Output: ["Ali", "Sara", "Tom"]

users = [
  {"name": "Ali", "age": 20},
  {"name": "Sara", "age": 22},
  {"name": "Tom", "age": 19}
]
users_names = list(map(lambda user: user["name"], users))
print(users_names)

# Multiply corresponding items & return as tuple list
# Input: [1,2,3] and [4,5,6]
# Output: [(1,4,4), (2,5,10), (3,6,18)]

nums_1 = [1, 2, 3]
nums_2 = [4, 5, 6]
nums_tuples = list(map(lambda n1, n2: (n1, n2, n1 * n2), nums_1, nums_2))
print(nums_tuples)

# Replace spaces with hyphens
# Input: ["hello world", "python is fun"]
# Output: ["hello-world", "python-is-fun"]

phrases = ["hello world", "python is fun"]
phrases_with_hyphens = list(map(lambda phrase: phrase.replace(" ", "-"), phrases))
print(phrases_with_hyphens)

# Square only even numbers
# Input: [1,2,3,4,5,6]

nums = [1, 2, 3, 4, 5, 6]
nums_square_even = list(map(lambda num: num * num, (filter(lambda num: num % 2 == 0, nums))))
print(nums_square_even)

# Convert only positive numbers to strings
# Input: [-3, 0, 2, 5, -1, 7]
# Expected: ["2", "5", "7"]

nums = [-3, 0, 2, 5, -1, 7]
posit_nums_str = list(map(lambda num: str(num), (filter(lambda num: num > 0, nums))))
print(posit_nums_str)

# Add 5 to numbers that are divisible by 3
# Input: [3, 4, 6, 8, 9, 10, 12]
# Expected: [8, 11, 14, 17]

nums = [3, 4, 6, 8, 9, 10, 12]
nums_add_5_div_3 = list(map(lambda num: num + 5, (filter(lambda num: num % 3 == 0, nums))))
print(nums_add_5_div_3)

# Extract ages above 18 and turn them into "Age: X"
# Input: people = [
#   {"name": "Ali", "age": 17},
#   {"name": "Sara", "age": 21},
#   {"name": "Tom", "age": 19}
# ]
# Output: ["Age: 21", "Age: 19"]

people = [
  {"name": "Ali", "age": 17},
  {"name": "Sara", "age": 21},
  {"name": "Tom", "age": 19}
]

# people_ages_more_18 = list(map(lambda person: f"Age: {person["age"]}", (filter(lambda person: person["age"] > 18, people))))
# print(people_ages_more_18)

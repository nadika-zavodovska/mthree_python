from itertools import count, cycle, repeat, chain, islice, takewhile

# Pure iterator usage

nums = [1, 2, 3, 4]

it = iter(nums)

# while True:
#     try:
#         print(next(it))
#     except StopIteration:
#         print("Done")
#         break

# Using the same list, only print names longer than 3 characters using next() and a loop
names = ["Anna", "Bob", "Chris"]
it_names = iter(names)

# while True:
#     try:
#         name = next(it_names)
#         if len(name) > 3:
#             print(f"Name: {name}")
#     except StopIteration:
#         print("Done")
#         break

# Use enumerate() and an iterator to print index + value from this list
fruits = ["apple","banana","kiwi"]
enum_iter = iter(enumerate(fruits))

# while True:
#     try:
#         index, fruit = next(enum_iter)
#         print(index, fruit)
#     except StopIteration:
#         print("Done")
#         break

# Using itertools.count(), print numbers from 10 to 15 (stop manually).
counter = count(10)

# while True:
#     num = next(counter)
#     print(num)
#     if num == 15:
#         print("Done")
#         break

# counter_every_3 = count(5, 3)
# printed = 0

# while printed < 5:
#     num = next(counter_every_3)
#     print(num)
#     printed += 1

# print("Done")

# Generate numbers starting at 10, step 2, and stop after you print 6 numbers.

# counter_num = count(10, 2)
# printed_num = 0

# while printed_num < 6:
#     print(next(counter_num))
#     printed_num += 1

# print("Done")

# Cycle through this list:
# colors_list = ["red", "green", "blue"]
# cycle_colors_list = cycle(colors_list)
# printed = 0

# while printed < 8:
#     print(next(cycle_colors_list))
#     printed += 1

# Use repeat("Python", 3) to pair each "Python" with numbers 0,1,2 using zip.
# repeat("Python", 3)

# with for loop
# for word, num in zip(repeat("Python", 3), range(3)):
#     print(f"{word} {num}")

# with while loop
# pairs = zip(repeat("Python", 3), range(3))
# pairs_iter = iter(pairs)

# while True:
#     try:
#         word, num = next(pairs_iter)
#         print(f"{word} {num}")
#     except StopIteration:
#         break

# Combine lists without using +:

# a = [1, 2, 3]
# b = [4, 5]
# c = [6]

# print(list(chain(a, b, c)))

# Print the first 5 numbers from range(100, 200) using islice()

# with fol loop
# for value in islice(range(100, 200), 5):
#     print(value)

# # with while loop
# slice_num = islice(range(100, 200), 5)

# while True:
#     try:
#         print(next(slice_num))
#     except StopIteration:
#         break

# Using takewhile, print numbers until one is >= 10
# with for loop
# nums = [1, 2, 3, 10, 11, 12]

# for num in takewhile(lambda x: x < 10, nums):
#     print(num)

# with while loop
nums = [1, 2, 3, 10, 11, 12]
it = iter(nums)

while True:
    try:
        value = next(it)
        if value < 10:
            print(value)
        else:
            break        
    except StopIteration:
        break
        

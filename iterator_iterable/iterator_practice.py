from itertools import count, cycle

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

# using itertools.cycle(), cycle through
colors = ["red", "green", "blue"]
iter_colors = iter(colors)
cycle_colors = cycle(iter_colors)
printed_colors = 0

while printed_colors < 5:
    print(next(cycle_colors))    
    printed_colors += 1

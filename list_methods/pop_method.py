# Remove the last element using pop() and store it in a variable called removed.
nums = [10, 20, 30, 40]

removed = nums.pop()
print(nums)
print(removed)

# ****

# Pop the element at index 1 (so remove "b") and print the remaining list.
letters = ["a", "b", "c", "d"]
letters.pop(1)
print(letters)

# ****
# Using a loop and pop(), remove items one by one and print them in the order they are removed.
stack = [1, 2, 3]

for num in range(len(stack)):
    print(stack.pop())

# ****
# Pop the last score
# Multiply it by 2
# Print the result

scores = [50, 60, 70]
print(scores.pop() * 2)
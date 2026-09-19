"""
Program: Maximum Consecutive Ones
Author: Aditya Keshri
Description: Finds the maximum number of consecutive 1s in a binary list.
"""

numbers = [1, 1, 0, 1, 1, 1, 0]

current_count = 0
maximum_count = 0

for num in numbers:

    if num == 1:
        current_count += 1

        if current_count > maximum_count:
            maximum_count = current_count

    else:
        current_count = 0

print("Numbers:", numbers)
print("Maximum Consecutive Ones:", maximum_count)
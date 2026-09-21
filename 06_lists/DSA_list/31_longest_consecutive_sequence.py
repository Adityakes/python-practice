"""
Program: Longest Consecutive Sequence
Author: Aditya Keshri
Description: Finds the length of the longest consecutive sequence in a list.
"""

numbers = [100, 4, 200, 1, 3, 2]

numbers_set = set(numbers)

longest = 0

for num in numbers_set:

    # Start only if num is the beginning of a sequence
    if num - 1 not in numbers_set:

        current = num
        length = 1

        while current + 1 in numbers_set:
            current += 1
            length += 1

        if length > longest:
            longest = length

print("Numbers:", numbers)
print("Longest Consecutive Sequence Length:", longest)
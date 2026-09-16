"""
Program: Move Zeroes
Author: Aditya Keshri
Description: Moves all zeroes to the end of the list while maintaining the order of other elements.
"""

numbers = [0, 1, 0, 3, 12]

result = []

for num in numbers:
    if num != 0:
        result.append(num)

zero_count = numbers.count(0)

for i in range(zero_count):
    result.append(0)

print("Original List:", numbers)
print("After Moving Zeroes:", result)
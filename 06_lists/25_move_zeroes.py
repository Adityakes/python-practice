"""
Program: Move All Zeroes to End
Author: Aditya Keshri
Description: Moves all zeroes to the end while maintaining
the order of non-zero elements.
"""

numbers = [0, 1, 0, 3, 12]

non_zero = []

for num in numbers:
    if num != 0:
        non_zero.append(num)

zero_count = numbers.count(0)

result = non_zero + [0] * zero_count

print("Original List:", numbers)
print("After Moving Zeroes:", result)
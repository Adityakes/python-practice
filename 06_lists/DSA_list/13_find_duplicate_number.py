"""
Program: Find Duplicate Number
Author: Aditya Keshri
Description: Finds the duplicate element present in a list.
"""

numbers = [1, 3, 4, 2, 2]

seen = set()

for num in numbers:
    if num in seen:
        print("Duplicate Number:", num)
        break

    seen.add(num)
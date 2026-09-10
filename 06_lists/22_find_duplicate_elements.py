"""
Program: Find Duplicate Elements in a List
Author: "Aditya Keshri"
Description: Finds elements that occur more than once.
"""

numbers = [10, 20, 10, 30, 20, 40, 10]

duplicates = []

for num in numbers:
    if numbers.count(num) > 1 and num not in duplicates:
        duplicates.append(num)

print("Original List:", numbers)
print("Duplicate Elements:", duplicates)
"""
Program: Remove Duplicates from Sorted List
Author: Aditya Keshri
Description: Removes duplicate elements from a sorted list.
"""

numbers = [1, 1, 2, 2, 3, 4, 4]

result = []

for num in numbers:
    if num not in result:
        result.append(num)

print("Original List:", numbers)
print("After Removing Duplicates:", result)
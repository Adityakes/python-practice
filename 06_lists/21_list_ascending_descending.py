"""
Program: Sort a List in Ascending and Descending Order
Author: "Aditya Keshri"
Description: Demonstrates ascending and descending sorting.
"""

numbers = [40, 10, 30, 50, 20]

ascending = sorted(numbers)
descending = sorted(numbers, reverse=True)

print("Original List:", numbers)
print("Ascending Order:", ascending)
print("Descending Order:", descending)
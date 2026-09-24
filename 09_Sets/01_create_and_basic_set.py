"""
Program: Create and Basic Set Operations
Author: Aditya Keshri
Description: Creates a set and demonstrates basic set operations.
"""

numbers = {10, 20, 30, 40, 50}

print("Set:", numbers)
print("Number of Elements:", len(numbers))

numbers.add(60)

print("After Adding 60:", numbers)

numbers.remove(30)

print("After Removing 30:", numbers)
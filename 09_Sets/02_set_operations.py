"""
Program: Set Operations
Author: Aditya Keshri
Description: Demonstrates union, intersection, and difference operations on sets.
"""

set1 = {10, 20, 30, 40, 50}
set2 = {40, 50, 60, 70, 80}

union = set1 | set2
intersection = set1 & set2
difference = set1 - set2

print("Set 1:", set1)
print("Set 2:", set2)

print("Union:", union)
print("Intersection:", intersection)
print("Difference:", difference)
"""
Program: Tuple Element Frequency
Author: Aditya Keshri
Description: Counts how many times a given element occurs in a tuple.
"""

numbers = (10, 20, 10, 30, 10, 40, 20)
target = 10

count = 0

for num in numbers:
    if num == target:
        count += 1

print("Tuple:", numbers)
print("Target Element:", target)
print("Frequency:", count)
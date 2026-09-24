"""
Program: Maximum and Minimum in Tuple
Author: Aditya Keshri
Description: Finds the maximum and minimum elements from a tuple.
"""

numbers = (45, 12, 78, 23, 56, 9)

maximum = numbers[0]
minimum = numbers[0]

for num in numbers:

    if num > maximum:
        maximum = num

    if num < minimum:
        minimum = num

print("Tuple:", numbers)
print("Maximum:", maximum)
print("Minimum:", minimum)
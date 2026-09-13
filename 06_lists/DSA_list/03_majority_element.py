"""
Program: Majority Element
Author: Aditya Keshri
Description: Finds the element that appears more than n/2 times.
"""

numbers = [2, 2, 1, 1, 1, 2, 2]

for num in numbers:
    if numbers.count(num) > len(numbers) // 2:
        print("Majority Element:", num)
        break
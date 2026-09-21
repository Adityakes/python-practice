"""
Program: Find Peak Element
Author: Aditya Keshri
Description: Finds an element that is greater than its neighboring elements using binary search.
"""

numbers = [1, 2, 3, 1]

low = 0
high = len(numbers) - 1

while low < high:

    mid = (low + high) // 2

    if numbers[mid] < numbers[mid + 1]:
        low = mid + 1
    else:
        high = mid

print("Numbers:", numbers)
print("Peak Element:", numbers[low])
print("Peak Index:", low)
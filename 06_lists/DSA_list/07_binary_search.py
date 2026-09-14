
"""
Program: Binary Search
Author: Aditya Keshri
Description: Searches for an element in a sorted list using binary search.
"""

numbers = [1, 3, 5, 7, 9, 11]
target = 7

low = 0
high = len(numbers) - 1

while low <= high:
    mid = (low + high) // 2

    if numbers[mid] == target:
        print("Element found at index:", mid)
        break

    elif numbers[mid] < target:
        low = mid + 1

    else:
        high = mid - 1
else:
    print("Element not found")
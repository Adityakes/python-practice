"""
Program: Last Occurrence Using Binary Search
Author: Aditya Keshri
Description: Finds the last occurrence of a target element in a sorted list.
"""

numbers = [1, 2, 2, 2, 4, 5]
target = 2

low = 0
high = len(numbers) - 1
answer = -1

while low <= high:

    mid = (low + high) // 2

    if numbers[mid] == target:
        answer = mid
        low = mid + 1

    elif numbers[mid] < target:
        low = mid + 1

    else:
        high = mid - 1

print("Numbers:", numbers)
print("Last Occurrence:", answer)
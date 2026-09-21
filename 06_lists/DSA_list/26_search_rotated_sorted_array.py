"""
Program: Search in Rotated Sorted Array
Author: Aditya Keshri
Description: Searches for a target element in a rotated sorted list using binary search.
"""

numbers = [4, 5, 6, 7, 0, 1, 2]
target = 0

low = 0
high = len(numbers) - 1
answer = -1

while low <= high:

    mid = (low + high) // 2

    if numbers[mid] == target:
        answer = mid
        break

    # Left half is sorted
    if numbers[low] <= numbers[mid]:

        if numbers[low] <= target < numbers[mid]:
            high = mid - 1
        else:
            low = mid + 1

    # Right half is sorted
    else:

        if numbers[mid] < target <= numbers[high]:
            low = mid + 1
        else:
            high = mid - 1

print("Numbers:", numbers)
print("Target:", target)
print("Target Index:", answer)
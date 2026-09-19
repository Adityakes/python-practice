"""
Program: Two Pointer Pair Sum
Author: Aditya Keshri
Description: Finds a pair of elements with the given sum using the two-pointer technique.
"""

numbers = [1, 2, 3, 4, 6]
target = 6

left = 0
right = len(numbers) - 1

while left < right:

    current_sum = numbers[left] + numbers[right]

    if current_sum == target:
        print("Pair:", numbers[left], numbers[right])
        break

    elif current_sum < target:
        left += 1

    else:
        right -= 1
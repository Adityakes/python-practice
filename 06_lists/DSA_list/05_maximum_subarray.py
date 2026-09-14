"""
Program: Maximum Subarray
Author: Aditya Keshri
Description: Finds the maximum sum of a continuous subarray.
"""

numbers = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

current_sum = 0
maximum_sum = 0

for num in numbers:
    current_sum += num

    if current_sum < 0:
        current_sum = 0

    if current_sum > maximum_sum:
        maximum_sum = current_sum

print("Numbers:", numbers)
print("Maximum Subarray Sum:", maximum_sum)
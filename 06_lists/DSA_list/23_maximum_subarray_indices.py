"""
Program: Maximum Subarray with Indices
Author: Aditya Keshri
Description: Finds the maximum sum subarray and its starting and ending indices.
"""

numbers = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

current_sum = 0
maximum_sum = numbers[0]

start = 0
best_start = 0
best_end = 0

for i in range(len(numbers)):

    current_sum += numbers[i]

    if current_sum > maximum_sum:
        maximum_sum = current_sum
        best_start = start
        best_end = i

    if current_sum < 0:
        current_sum = 0
        start = i + 1

print("Numbers:", numbers)
print("Maximum Sum:", maximum_sum)
print("Start Index:", best_start)
print("End Index:", best_end)
print("Maximum Subarray:", numbers[best_start:best_end + 1])
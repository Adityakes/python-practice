"""
Program: Sliding Window
Author: Aditya Keshri
Description: Finds the maximum sum of a subarray of size k using the sliding window technique.
"""

numbers = [2, 1, 5, 1, 3, 2]
k = 3

window_sum = sum(numbers[:k])
maximum_sum = window_sum

for i in range(k, len(numbers)):
    window_sum = window_sum + numbers[i] - numbers[i - k]

    if window_sum > maximum_sum:
        maximum_sum = window_sum

print("Numbers:", numbers)
print("Window Size:", k)
print("Maximum Sum:", maximum_sum)
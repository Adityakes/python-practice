"""
Program: Prefix Sum
Author: Aditya Keshri
Description: Calculates the sum of elements in a given range using prefix sum.
"""

numbers = [2, 4, 6, 8, 10]

prefix = [0]

for num in numbers:
    prefix.append(prefix[-1] + num)

left = 1
right = 3

range_sum = prefix[right + 1] - prefix[left]

print("Numbers:", numbers)
print("Prefix Sum:", prefix)
print("Range Sum:", range_sum)
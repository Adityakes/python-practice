"""
Program: Subarray Sum Equals K
Author: Aditya Keshri
Description: Counts the number of continuous subarrays whose sum equals the target k.
"""

numbers = [1, 2, 3]
k = 3

prefix_sum = 0
count = 0
seen = {0: 1}

for num in numbers:

    prefix_sum += num

    required = prefix_sum - k

    if required in seen:
        count += seen[required]

    seen[prefix_sum] = seen.get(prefix_sum, 0) + 1

print("Numbers:", numbers)
print("Target:", k)
print("Number of Subarrays:", count)
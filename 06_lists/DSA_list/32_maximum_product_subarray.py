"""
Program: Maximum Product Subarray
Author: Aditya Keshri
Description: Finds the maximum product of a continuous subarray.
"""

numbers = [2, 3, -2, 4]

current_max = numbers[0]
current_min = numbers[0]
maximum_product = numbers[0]

for i in range(1, len(numbers)):

    num = numbers[i]

    if num < 0:
        current_max, current_min = current_min, current_max

    current_max = max(num, current_max * num)
    current_min = min(num, current_min * num)

    maximum_product = max(maximum_product, current_max)

print("Numbers:", numbers)
print("Maximum Product:", maximum_product)
"""
Program: Product of Array Except Self
Author: Aditya Keshri
Description: Creates a new list where each element is the product of all other elements.
"""

numbers = [1, 2, 3, 4]

result = [1] * len(numbers)

prefix = 1

for i in range(len(numbers)):
    result[i] = prefix
    prefix *= numbers[i]

suffix = 1

for i in range(len(numbers) - 1, -1, -1):
    result[i] *= suffix
    suffix *= numbers[i]

print("Numbers:", numbers)
print("Product Except Self:", result)
"""
Program: Missing Number
Author: Aditya Keshri
Description: Finds the missing number from 0 to n.
"""

numbers = [3, 0, 1]

n = len(numbers)

expected_sum = n * (n + 1) // 2
actual_sum = sum(numbers)

missing = expected_sum - actual_sum

print("Numbers:", numbers)
print("Missing Number:", missing)
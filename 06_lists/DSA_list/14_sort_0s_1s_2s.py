"""
Program: Sort 0s, 1s and 2s
Author: Aditya Keshri
Description: Sorts a list containing only 0s, 1s and 2s.
"""

numbers = [2, 0, 2, 1, 1, 0]

count_0 = numbers.count(0)
count_1 = numbers.count(1)
count_2 = numbers.count(2)

result = []

for i in range(count_0):
    result.append(0)

for i in range(count_1):
    result.append(1)

for i in range(count_2):
    result.append(2)

print("Original List:", numbers)
print("Sorted List:", result)
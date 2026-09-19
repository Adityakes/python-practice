"""
Program: Majority Element Using Boyer-Moore
Author: Aditya Keshri
Description: Finds the majority element using the Boyer-Moore Voting Algorithm.
"""

numbers = [2,1,1, 2, 1, 1, 1, 2, 2]

candidate = None
count = 0

for num in numbers:

    if count == 0:
        candidate = num

    if num == candidate:
        count += 1
    else:
        count -= 1

print("Majority Element:", candidate)
"""
Program: Pair with Given Sum
Author: Aditya Keshri
Description: Finds a pair of numbers whose sum equals the target.
"""

numbers = [2, 7, 11, 15]
target = 9

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] == target:
            print("Pair:", numbers[i], numbers[j])
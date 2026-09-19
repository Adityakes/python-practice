"""
Program: Move Zeroes Using Two Pointers
Author: Aditya Keshri
Description: Moves all zeroes to the end of the list using the two-pointer technique.
"""

numbers = [0, 1, 0, 3, 12]

left = 0

for right in range(len(numbers)):

    if numbers[right] != 0:
        numbers[left], numbers[right] = numbers[right], numbers[left]
        left += 1

print("After Moving Zeroes:", numbers)
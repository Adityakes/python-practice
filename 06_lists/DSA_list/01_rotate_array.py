"""
Program: Rotate Array
Author: Aditya Keshri
Description: Rotates the list to the right by k positions.
"""

numbers = [1, 2, 3, 4, 5]
k = 2

k = k % len(numbers)

result = numbers[-k:] + numbers[:-k]

print("Original List:", numbers)
print("Rotated List:", result)


'''
Original: [1, 2, 3, 4, 5]
k = 2

Output:   [4, 5, 1, 2, 3]
'''
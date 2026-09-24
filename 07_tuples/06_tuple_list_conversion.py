"""
Program: Tuple and List Conversion
Author: Aditya Keshri
Description: Converts a tuple into a list and a list into a tuple.
"""

numbers_tuple = (10, 20, 30, 40)

numbers_list = list(numbers_tuple)

print("Original Tuple:", numbers_tuple)
print("Converted List:", numbers_list)

numbers_list.append(50)

new_tuple = tuple(numbers_list)

print("Updated List:", numbers_list)
print("New Tuple:", new_tuple)
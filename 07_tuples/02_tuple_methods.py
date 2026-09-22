"""
Program: Tuple Methods
Author: Aditya Keshri
Description: Demonstrates count() and index() methods of a tuple.
"""

numbers = (10, 20, 10, 30, 40, 10)

count_10 = numbers.count(10)
index_30 = numbers.index(30)

print("Tuple:", numbers)
print("Count of 10:", count_10)
print("Index of 30:", index_30)
"""
Program: Comparison Operators
Author: Aditya Keshri
Description: Comparison operators in Python
"""

a = 10
b = 20

print("a =", a)
print("b =", b)
print()

print("a == b :", a == b)
print("a != b :", a != b)
print("a > b  :", a > b)
print("a < b  :", a < b)
print("a >= b :", a >= b)
print("a <= b :", a <= b)

age = int(input("Enter your age: "))

print("Eligible for voting:", age >= 18)
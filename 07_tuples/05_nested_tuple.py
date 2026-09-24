"""
Program: Nested Tuple
Author: Aditya Keshri
Description: Demonstrates how to create and access elements from a nested tuple.
"""

students = (
    ("Aditya", 85),
    ("Rahul", 78),
    ("Aman", 92)
)

print("Students:", students)

print("First Student:", students[0])
print("First Student Name:", students[0][0])
print("First Student Marks:", students[0][1])

print("Second Student Name:", students[1][0])
print("Second Student Marks:", students[1][1])
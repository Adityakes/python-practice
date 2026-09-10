"""
Program: Insert and Delete Elements from a List
Author: "Aditya Keshri"
Description: Demonstrates insert(), remove() and pop() methods.
"""

numbers = [10, 20, 30, 40, 50]

print("Original List:", numbers)

# Insert 25 at index 2
numbers.insert(2, 25)
print("After Inserting 25:", numbers)

# Remove element 30
numbers.remove(30)
print("After Removing 30:", numbers)

# Remove last element
removed_element = numbers.pop()
print("Removed Element:", removed_element)
print("Final List:", numbers)
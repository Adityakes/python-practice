"""
Program: String Methods
Author: Aditya Keshri
Description: Common String Methods in Python
"""

name = "aditya keshri"

print("Original :", name)

print("Upper    :", name.upper())
print("Lower    :", name.lower())
print("Title    :", name.title())
print("Capitalize:", name.capitalize())

print()

print("Replace      :", name.replace("a", "@"))
print("Find         :", name.find("keshri"))
print("Count        :", name.count("a"))
print("Startswith   :", name.startswith("aditya"))
print("Endswith     :", name.endswith("keshri"))


name = "  Python Programming  "

print(len(name))
print(name.strip())
print(len(name.strip()))


text = "Python"

print(text * 3)
print("-" * 20)
print(text + " Programming")
"""
Program: Dictionary Basics
Description: Basic operations with Python dictionaries
"""

student = {
    "name": "Aditya",
    "course": "B.Tech CSE",
    "year": 3
}

print("Student:", student)
print("Name:", student["name"])
print("Course:", student["course"])

student["city"] = "Bihar"

print("Updated Student:", student)

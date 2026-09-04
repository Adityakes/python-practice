"""
Author: Aditya Keshri
Program: Subject Marks using **kwargs
Description: Practice handling multiple subject marks
"""

def show_marks(**marks):
    for subject, mark in marks.items():
        print(subject, ":", mark)


show_marks(
    Python=85,
    DBMS=78,
    DSA=82,
    Mathematics=75
)
"""
Program: args_operations
Author: Aditya Keshri
Description: Understanding args_operations
"""

def calculate(*numbers):
    total = sum(numbers)
    maximum = max(numbers)
    minimum = min(numbers)

    print("Numbers:", numbers)
    print("Total:", total)
    print("Maximum:", maximum)
    print("Minimum:", minimum)


calculate(10, 20, 30, 40, 50)
"""
Program: 13_args_basics
Author: Aditya Keshri
Description: Understanging args
"""


# *args allows a function to accept multiple positional arguments

def add_numbers(*args):
    total = 0

    for num in args:
        total += num

    return total


print(add_numbers(10, 20))
print(add_numbers(10, 20, 30))
print(add_numbers(1, 2, 3, 4, 5))
"""
Program: *args Practice
Author: Aditya Keshri
Description: Simple practice with variable-length arguments
"""


def show_numbers(*numbers):
    for number in numbers:
        print(number)


show_numbers(10, 20, 30, 40, 50)
"""
Program: Function Basics
Author: Aditya Keshri
Description: Basic examples of Python functions
"""
# Program - Square of a Number

def square(number):
    print("Square of number:", number * number)


square(7)


# Program - Square using User Input

def square_number(number):
    print("Square of number:", number ** 2)


num = int(input("Enter a number: "))
square_number(num)

"""
Program: Function Basics
Author: Aditya Keshri
Description: Basic examples of Python functions
"""
# Program - Check Even or Odd

def is_even(number):
    if number % 2 == 0:
        print("Even Number")
    else:
        print("Odd Number")


num = int(input("Enter your number: "))
is_even(num)
"""
Program: Function Basics
Author: Aditya Keshri
Description: Basic examples of Python functions
"""
# Program - Find Largest of Two Numbers

def largest_two(a, b):
    if a > b:
        print("A is largest:", a)
    else:
        print("B is largest:", b)


num_a = int(input("Enter 1st number: "))
num_b = int(input("Enter 2nd number: "))

largest_two(num_a, num_b)


# Program - Find Largest of Three Numbers

def largest_three(a, b, c):
    if a > b and a > c:
        print("A is largest:", a)
    elif b > a and b > c:
        print("B is largest:", b)
    else:
        print("C is largest:", c)


num_a = int(input("Enter 1st number: "))
num_b = int(input("Enter 2nd number: "))
num_c = int(input("Enter 3rd number: "))

largest_three(num_a, num_b, num_c)

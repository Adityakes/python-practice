"""
Program: *args
Author: Aditya Keshri
Description: Understanding variable-length arguments using *args with user input
"""


# Example 1 - Multiple Arguments

def add_numbers(*numbers):
    total = 0

    for number in numbers:
        total = total + number

    return total


result = add_numbers(10, 20, 300)

print("Sum:", result)


# Example 2 - User Input with *args

user_input = input("Enter numbers separated by space: ")

numbers = list(map(int, user_input.split()))

result = add_numbers(*numbers)

print("User Input Sum:", result)
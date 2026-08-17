"""
Program: Return Statement
Author: Aditya Keshri
Description: Examples of using return in Python functions
"""

# Program 1 - Return Square

def square(number):
    return number ** 2


num = int(input("Enter a number for square: "))

result = square(num)

print("Square:", result)


# Program 2 - Return Cube

def cube(number):
    return number ** 3


num = int(input("Enter a number for cube: "))

result = cube(num)

print("Cube:", result)


# Program 3 - Return Sum

def add(a, b):
    return a + b


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result = add(num1, num2)

print("Sum:", result)


# Program 4 - Return Multiplication

def multiply(a, b):
    return a * b


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result = multiply(num1, num2)

print("Product:", result)


# Program 5 - Return Value Used Further

def calculate(a, b):
    return a + b


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result = calculate(num1, num2)

final_result = result * 2

print("Final Result:", final_result)


# Program 6 - Return Multiple Values

def calculate_values(a, b):
    return a + b, a - b


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

sum_result, difference_result = calculate_values(num1, num2)

print("Sum:", sum_result)
print("Difference:", difference_result)
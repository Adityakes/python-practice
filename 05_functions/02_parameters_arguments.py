"""
Program: Parameters and Arguments
Author: Aditya Keshri
Description: Examples of parameters, arguments and user input
"""

# Program 1 - Single Parameter

def greet(name):
    print("Hello", name)


greet("Aditya")


# Program 2 - Multiple Parameters

def greet_name(first_name, last_name):
    print("Hello", first_name, last_name)


greet_name("Aditya", "Keshri")


# Program 3 - Parameters with User Input

def greet_user(first_name, last_name):
    print("Hello", first_name, last_name)


first = input("Enter First Name: ")
last = input("Enter Your Last Name: ")

greet_user(first, last)
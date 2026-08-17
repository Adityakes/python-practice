"""
Program: Default Parameters
Author: Aditya Keshri
Description: Examples of default parameter values in functions
"""

# Program 1 - Default Parameter

def welcome(name="Guest"):
    print("Welcome", name)


welcome()
welcome("Aditya")


# Program 2 - Multiple Default Parameters

def greet(name="User", message="Hello"):
    print(message, name)


greet()
greet("Aditya")
greet("Aditya", "Welcome")


# Program 3 - Student Information

def student(name="Unknown", course="Python"):
    print("Student:", name)
    print("Course:", course)


student()


# Program 4 - Student Information with User Input

stu = input("Enter your name: ")
crs = input("Enter your course: ")

student(stu, crs)
"""
Program: LEGB Scope
Author: Aditya Keshri
Description: Understanding Local, Enclosing, Global and Built-in scopes
"""


# 1. Local Scope

def local_example():
    number = 10
    print("Local:", number)


local_example()


# 2. Enclosing Scope

def outer():
    message = "Enclosing"

    def inner():
        print("Enclosing:", message)

    inner()


outer()


# 3. Global Scope

name = "Aditya"


def global_example():
    print("Global:", name)


global_example()


# 4. Built-in Scope

def builtin_example():
    text = "Python"
    print("Length:", len(text))


builtin_example()


# 5. LEGB Search Order Example

x = "Global"


def outer_function():
    x = "Enclosing"

    def inner_function():
        x = "Local"
        print("LEGB:", x)

    inner_function()


outer_function()
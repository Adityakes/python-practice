"""
Program: Variable Scope
Author: Aditya Keshri
Description: Understanding local and global variables in Python
"""


# Program 1 - Local Variable

def calculate():
    number = 50
    print(number)


calculate()


# Program 2 - Global Variable

x = 100


def show_global():
    print(x)


show_global()
print(x)


# Program 3 - Local and Global Variables with Same Name

x = 10


def test():
    x = 20
    print("Inside function:", x)


test()

print("Outside function:", x)


# Program 4 - Modifying Global Variable

count = 5


def update():
    global count
    count = count + 1


update()

print("Updated count:", count)


# Program 5 - Global and Local Variable Together

x = 10


def change():
    global x
    x = 50
    y = 100

    print("Inside function - x:", x)
    print("Inside function - y:", y)


change()

print("Outside function - x:", x)
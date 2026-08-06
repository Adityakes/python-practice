"""
Program: For Loop Basics
Author: Aditya Keshri
Description: Print numbers using for loop
"""

# Program 1: Print 1 to 10
for i in range(1, 11):
    print(i)

# Program 2: Print 10 to 1
for i in range(10, 0, -1):
    print(i)

# Program 3: Even Numbers
for i in range(2, 21, 2):
    print(i)

# Program 4: Odd Numbers
for i in range(1, 20, 2):
    print(i)

# Program 5: Table of 5
for i in range(1, 11):
    print("5 x", i, "=", 5 * i)

# Program 6: User Input Table ⭐
num = int(input("Enter a number: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)



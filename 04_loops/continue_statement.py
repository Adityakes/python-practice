"""
Program: Continue Statement
Author: Aditya Keshri
Description: Examples of using the continue statement
"""

# Program 1 - Skip number 5

for i in range(1, 11):
    if i == 5:
        continue
    print(i)


print("\nProgram 2 - Print even numbers")


# Program 2 - Skip odd numbers

for i in range(1, 11):
    if i % 2 != 0:
        continue
    print(i)


print("\nProgram 3 - Skip negative numbers")


# Program 3 - Skip negative numbers

for i in range(1, 6):
    num = int(input("Enter number: "))

    if num < 0:
        continue

    print(num)


print("\nProgram 4 - Skip multiples of 5")


# Program 4 - Skip multiples of 5

for i in range(1, 21):
    if i % 5 == 0:
        continue
    print(i)
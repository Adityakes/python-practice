"""
Program: Pass Statement
Author: Aditya Keshri
Description: Examples of using the pass statement
"""

# Program 1 - Basic pass

for i in range(1, 6):
    if i == 3:
        pass
    print(i)


print("\nProgram 2 - Pass at 5")


# Program 2 - Pass at 5

for i in range(1, 11):
    if i == 5:
        pass
    print(i)


print("\nProgram 3 - Pass with even numbers")


# Program 3 - Pass with even numbers

for i in range(1, 11):
    if i % 2 == 0:
        pass
    else:
        print("Odd number:", i)
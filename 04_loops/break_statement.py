"""
Program: Break Statement
Author: Aditya Keshri
Description: Stop a loop using break statement
"""

i = 1

while i <= 10:
    if i == 4:
        break

    print(i)
    i = i + 1

print("Loop ended")
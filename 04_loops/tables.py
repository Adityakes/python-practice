"""
Program: For Loop Basics
Author: Aditya Keshri
Description: Print Tables using for loop
"""
# 5TH Table
for i in range(1, 11):
   print("5 x", i, "=", 5 * i)


# Input Taken From User For Writing Table
num = int(input("Enter a number: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)
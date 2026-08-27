'''
Author: "Aditya Keshri"

Program: Print Floyd's Triangle

Output:

1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
'''


def floyds_triangle(n):
    number = 1

    for i in range(1, n + 1):
        for j in range(i):
            print(number, end=" ")
            number += 1
        print()


floyds_triangle(5)
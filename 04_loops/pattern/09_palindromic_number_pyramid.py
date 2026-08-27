'''
Author: "Aditya Keshri"

Program: Print Palindromic Number Pyramid

Output:

    1
   121
  12321
 1234321
123454321
'''


def palindromic_number_pyramid(n):

    for i in range(1, n + 1):

        # Print spaces
        for j in range(n - i):
            print(" ", end="")

        # Print increasing numbers
        for j in range(1, i + 1):
            print(j, end="")

        # Print decreasing numbers
        for j in range(i - 1, 0, -1):
            print(j, end="")

        print()


palindromic_number_pyramid(5)
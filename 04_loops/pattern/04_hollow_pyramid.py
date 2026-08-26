'''
Author: "Aditya Keshri"
Program: Print Butterfly Pattern

Output:
    *
   * *
  *   *
 *     *
*********

'''


def hollow_pyramid(n):
    for i in range(1, n + 1):
        # Spaces
        for j in range(n - i):
            print(" ", end="")

        # Stars
        for j in range(2 * i - 1):
            if j == 0 or j == 2 * i - 2 or i == n:
                print("*", end="")
            else:
                print(" ", end="")

        print()


hollow_pyramid(5)
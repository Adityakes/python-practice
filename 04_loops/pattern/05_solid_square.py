'''
Author: "Aditya Keshri"
program: "solid_square"
Output:
*****             
*****
*****
*****             
*****
'''

def solid_square(n):
    for i in range(n):
        for j in range(n):
            print("*", end="")
        print()


solid_square(5)
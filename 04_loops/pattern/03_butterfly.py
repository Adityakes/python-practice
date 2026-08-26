'''
Author: "Aditya Keshri"
Program: Print Butterfly Pattern

Output:
*             *
**           **
***         ***
****       ****
*****     *****
******   ******
******* *******
***************
******* *******
******   ******
*****     *****
****       ****

'''
# Program
def butterfly(n):
    for i in range(2*n-1):
        for j in range(2*n-1):
            h=i if i<n else 2*n-2-i
            if j<=h or j>=2*n-2-h:
                print("*",end="")
            else:
                print(" ", end="")
        print()
butterfly(8)
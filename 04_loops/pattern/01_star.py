'''
Author "Aditya Keshri"
program : Increasing Star pattern
* 
* * 
* * * 
* * * * 
* * * * * 
'''
for i in range(1, 6):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()


# Program 2 - Reverse Star Pattern
'''
* * * * *
* * * *
* * *
* *
*
'''

for i in range(5, 0, -1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()
"""
Program: Strings
Author: Aditya Keshri
Description: Introduction to Strings in Python
"""

# Creating Strings

name = "Name: Aditya"
city = 'City: Meerut'
college = "College: ABSS Institute of Technology"

print(name)
print(city)
print(college)

print(type(name))


# String Indexing

name = "Aditya"

print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])

'''
String =  A  d  i  t  y  a
Index  =  0  1  2  3  4  5
         -6 -5 -4 -3 -2 -1 

'''

# Assignment (Negative Indexing Starts form endside)
print(name[-1])
print(name[-2])

'''
Output:- 
-1 = a
-2 = y

'''


# String Slicing

name = "Aditya"

print(name[0:3])
print(name[2:5])
print(name[:4])
print(name[2:])
print(name[:])

'''
Output:-
1 = Adi
2 = ity
3 = Adit
4 = itya
5 = Aditya
'''

# String Methods

name = "aditya keshri"

print(name.upper())
print(name.lower())
print(name.title())
print(name.capitalize())

print(name.replace("aditya", "Aditya"))
print(name.find("keshri"))
print(len(name))




# ==========================
# Notes
# ==========================
# 1. Strings are immutable.
# 2. Indexing starts from 0.
# 3. Negative indexing starts from -1.
# 4. End index is excluded in slicing.
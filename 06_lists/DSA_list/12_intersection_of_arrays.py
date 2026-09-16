"""
Program: Intersection of Two Arrays
Author: Aditya Keshri
Description: Finds the common elements present in two lists.
"""

list1 = [1, 2, 2, 3, 4]
list2 = [2, 2, 4, 5]

result = []

for num in list1:
    if num in list2 and num not in result:
        result.append(num)

print("List 1:", list1)
print("List 2:", list2)
print("Common Elements:", result)
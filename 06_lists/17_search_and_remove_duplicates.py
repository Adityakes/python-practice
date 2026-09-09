'''
Program: search and remove duplicate Numbers
Author: "Aditya Keshri"
Description: Finds And Remove The Duplicate Numbers

'''


numbers = [10, 20, 10, 30, 20, 40]

# Search
search_element = 30

if search_element in numbers:
    print(search_element, "is present in the list")
else:
    print(search_element, "is not present in the list")


# Remove duplicates
unique_numbers = list(set(numbers))

print("Original List:", numbers)
print("List without duplicates:", unique_numbers)
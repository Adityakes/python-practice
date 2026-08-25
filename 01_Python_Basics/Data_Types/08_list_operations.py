"""
Program: List Operations
Description: Practicing basic list operations
"""

numbers = [10, 20, 30, 40]

print("Original list:", numbers)

numbers.append(50)
print("After append:", numbers)

numbers.remove(20)
print("After remove:", numbers)

numbers.sort(reverse=True)
print("After sorting:", numbers)

print("List length:", len(numbers))
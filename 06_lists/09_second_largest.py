# Create a list
numbers = [10, 45, 23, 67, 89, 34, 89, 12]

# Remove duplicate values
unique_numbers = list(set(numbers))

# Sort the list
unique_numbers.sort()

# Find the second largest element
second_largest = unique_numbers[-2]

print("List:", numbers)
print("Second largest element:", second_largest)
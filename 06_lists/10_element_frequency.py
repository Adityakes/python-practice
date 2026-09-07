# Create a list
numbers = [10, 20, 10, 30, 20, 10, 40, 30, 20]

frequency = {}

# Count frequency of each element
for number in numbers:
    if number in frequency:
        frequency[number] += 1
    else:
        frequency[number] = 1

# Display frequency
for number, count in frequency.items():
    print(number, "->", count)
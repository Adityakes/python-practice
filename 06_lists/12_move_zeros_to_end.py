numbers = [0, 5, 0, 3, 8, 0, 2, 0, 7]

result = []

# Add all non-zero elements
for number in numbers:
    if number != 0:
        result.append(number)

# Count zeros
zero_count = numbers.count(0)

# Add zeros at the end
result.extend([0] * zero_count)

print("Original list:", numbers)
print("After moving zeros:", result)
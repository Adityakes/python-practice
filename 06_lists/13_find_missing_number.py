numbers = [1, 2, 3, 5, 6, 7, 8]

n = len(numbers) + 1

# Sum of numbers from 1 to n
expected_sum = n * (n + 1) // 2

# Sum of elements present in the list
actual_sum = sum(numbers)

# Missing number
missing = expected_sum - actual_sum

print("List:", numbers)
print("Missing number:", missing)
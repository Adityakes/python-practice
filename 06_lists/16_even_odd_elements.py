'''
Program: Odd And Even
Author: "Aditya Keshri"
Description: Finds The Odd And Even of the numbers
'''

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

even_numbers = []
odd_numbers = []

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)

print("Numbers:", numbers)
print("Even Numbers:", even_numbers)
print("Odd Numbers:", odd_numbers)
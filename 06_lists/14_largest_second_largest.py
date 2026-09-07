'''
program: " Largest_second_largest Number"
Author: "Aditya Keshri"
Description: "Find Largest and Second Largest Without max() / sort()"
'''



numbers = [25, 10, 45, 67, 34, 89, 52]

largest = float("-inf")
second_largest = float("-inf")

for number in numbers:
    if number > largest:
        second_largest = largest
        largest = number

    elif number > second_largest and number != largest:
        second_largest = number

print("List:", numbers)
print("Largest:", largest)
print("Second largest:", second_largest)
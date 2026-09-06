# Create a list
fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes"]

# Search for an element
search = input("Enter a fruit to search: ")

if search in fruits:
    print(search, "is present in the list.")
else:
    print(search, "is not present in the list.")
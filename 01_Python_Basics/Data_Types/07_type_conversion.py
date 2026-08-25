"""
Program: Type Conversion
Description: Basic Python type conversion practice
"""

number = "25"
decimal = "10.5"

integer_number = int(number)
float_number = float(decimal)
string_number = str(integer_number)

print("Integer:", integer_number)
print("Float:", float_number)
print("String:", string_number)

print("Integer type:", type(integer_number))
print("Float type:", type(float_number))
print("String type:", type(string_number))
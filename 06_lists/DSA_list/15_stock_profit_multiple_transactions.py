"""
Program: Stock Profit with Multiple Transactions
Author: Aditya Keshri
Description: Finds the maximum profit when multiple buy and sell transactions are allowed.
"""

prices = [7, 1, 5, 3, 6, 4]

maximum_profit = 0

for i in range(1, len(prices)):
    if prices[i] > prices[i - 1]:
        maximum_profit += prices[i] - prices[i - 1]

print("Prices:", prices)
print("Maximum Profit:", maximum_profit)
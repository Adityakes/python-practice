"""
Program: Best Time to Buy and Sell Stock
Author: Aditya Keshri
Description: Finds the maximum profit from one buy and one sell.
"""

prices = [7, 1, 5, 3, 6, 4]

minimum_price = prices[0]
maximum_profit = 0

for price in prices:
    if price < minimum_price:
        minimum_price = price

    profit = price - minimum_price

    if profit > maximum_profit:
        maximum_profit = profit

print("Prices:", prices)
print("Maximum Profit:", maximum_profit)
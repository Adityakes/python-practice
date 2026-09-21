"""
Program: Trapping Rain Water
Author: Aditya Keshri
Description: Calculates the amount of rainwater that can be trapped between bars.
"""

heights = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

left = 0
right = len(heights) - 1

left_max = 0
right_max = 0

water = 0

while left < right:

    if heights[left] <= heights[right]:

        if heights[left] >= left_max:
            left_max = heights[left]
        else:
            water += left_max - heights[left]

        left += 1

    else:

        if heights[right] >= right_max:
            right_max = heights[right]
        else:
            water += right_max - heights[right]

        right -= 1

print("Heights:", heights)
print("Trapped Rain Water:", water)
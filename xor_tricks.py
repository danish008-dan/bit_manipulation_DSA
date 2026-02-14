"""
Purpose:
--------
Demonstrate common XOR tricks used in interviews.
"""

# 1. Swap two numbers without temp variable
def swap(a, b):
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b


# 2. Find single number (others appear twice)
def single_number(nums):
    result = 0
    for num in nums:
        result ^= num
    return result


# Example
print("Swap:", swap(5, 7))
print("Single number:", single_number([4, 1, 2, 1, 2]))

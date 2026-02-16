"""
Purpose:
--------
In an array where every number appears twice
except two numbers, find those two numbers.

Example:
[1, 2, 1, 3, 2, 5]
Output: 3, 5
"""

def two_single_numbers(nums):
    xor_all = 0

    # Step 1: XOR all numbers
    for num in nums:
        xor_all ^= num

    # Step 2: Find rightmost set bit
    diff_bit = xor_all & -xor_all

    num1 = 0
    num2 = 0

    # Step 3: Divide numbers into two groups
    for num in nums:
        if num & diff_bit:
            num1 ^= num
        else:
            num2 ^= num

    return num1, num2


print(two_single_numbers([1, 2, 1, 3, 2, 5]))

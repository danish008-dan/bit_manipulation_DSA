"""
Purpose:
--------
Given numbers from 0 to n with one number missing,
find the missing number.

Example:
[3, 0, 1] -> Missing = 2
"""

def missing_number(nums):
    n = len(nums)
    xor_all = 0

    # XOR all indices and numbers
    for i in range(n):
        xor_all ^= i ^ nums[i]

    xor_all ^= n
    return xor_all


print(missing_number([3, 0, 1]))

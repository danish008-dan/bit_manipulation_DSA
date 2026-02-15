"""
Purpose:
--------
Count number of set bits (1s) in binary representation
of a number using efficient method.
"""

def count_set_bits(n):
    count = 0

    while n:
        # Remove the lowest set bit
        n = n & (n - 1)
        count += 1

    return count


print("Set bits in 29:", count_set_bits(29))


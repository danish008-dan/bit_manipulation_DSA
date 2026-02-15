"""
Purpose:
--------
Check whether a number is a power of 2
using bit manipulation.
"""

def is_power_of_two(n):
    # Power of 2 has only one bit set
    return n > 0 and (n & (n - 1)) == 0


print("Is 16 power of 2?", is_power_of_two(16))
print("Is 18 power of 2?", is_power_of_two(18))

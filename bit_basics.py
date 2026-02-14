"""
Purpose:
--------
Demonstrate basic bit manipulation operations:

- Check if a bit is set
- Set a bit
- Clear a bit
- Toggle a bit

Bit positions are 0-indexed from right.
"""

def check_bit(n, pos):
    # Check if bit at position pos is 1
    return (n & (1 << pos)) != 0


def set_bit(n, pos):
    # Set bit at position pos to 1
    return n | (1 << pos)


def clear_bit(n, pos):
    # Clear bit at position pos (make it 0)
    return n & ~(1 << pos)


def toggle_bit(n, pos):
    # Flip bit at position pos
    return n ^ (1 << pos)


# Example
number = 10  # Binary: 1010

print("Check bit 1:", check_bit(number, 1))
print("Set bit 0:", set_bit(number, 0))
print("Clear bit 3:", clear_bit(number, 3))
print("Toggle bit 2:", toggle_bit(number, 2))

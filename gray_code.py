"""
Purpose:
--------
Generate n-bit Gray code sequence.

Property:
---------
Gray code ensures only ONE bit changes
between consecutive numbers.

Formula:
--------
Gray(i) = i ^ (i >> 1)
"""

def gray_code(n):
    result = []

    for i in range(1 << n):
        result.append(i ^ (i >> 1))

    return result


print(gray_code(3))

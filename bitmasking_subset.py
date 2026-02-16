"""
Purpose:
--------
Generate all subsets of a list using bitmasking.

Idea:
-----
If array size = n
Total subsets = 2^n

Each number from 0 to (2^n - 1) represents
a subset in binary form.
"""

def generate_subsets(nums):
    n = len(nums)
    total = 1 << n  # 2^n
    result = []

    for mask in range(total):
        subset = []

        for i in range(n):
            # Check if i-th bit is set
            if mask & (1 << i):
                subset.append(nums[i])

        result.append(subset)

    return result


# Example
nums = [1, 2, 3]
print(generate_subsets(nums))

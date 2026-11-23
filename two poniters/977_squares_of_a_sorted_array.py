"""
LeetCode 977 — Squares of a Sorted Array
"""


def sorted_squares(nums):
    n = len(nums)
    left =0
    right=n-1
    res=[0 for i in range(n)]

    for index in range(n-1,-1,-1):
        left_abs = abs(nums[left])
        right_abs=abs(nums[right])
        if left_abs >= right_abs:
            res[index]= left_abs*left_abs
            left+=1
        else:
            res[index]=right_abs*right_abs
            right-=1

    return res


# Main code
test_cases = [
    ([-4, -1, 0, 3, 10], [0, 1, 9, 16, 100]),
    ([-7, -3, 2, 3, 11], [4, 9, 9, 49, 121]),
    ([0], [0]),
    ([-5, -2, -1], [1, 4, 25]),
    ([1, 2, 3, 4, 5], [1, 4, 9, 16, 25])
]

count: int = 0

for nums, expected in test_cases:
    actual = sorted_squares(nums)

    print("Input:   ", nums)
    print("Expected:", expected)
    print("Actual:  ", actual)
    print("Result:  ", "PASS" if actual == expected else "FAIL")
    print()

    if actual == expected:
        count += 1

print(f'{count}/{5} PASSED')
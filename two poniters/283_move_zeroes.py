"""
LeetCode 283 — Move Zeroes
"""


def move_zeroes(nums):
    n = len(nums)
    left=0

    for right in range(n):
        if nums[right] != 0:
            temp = nums[left]
            nums[left]=nums[right]
            nums[right]=temp
            left+=1


    return nums



# Main code
test_cases = [
    ([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]),
    ([0, 0, 1], [1, 0, 0]),
    ([1, 2, 3], [1, 2, 3]),
    ([0, 0, 0], [0, 0, 0]),
    ([4, 0, 5, 0, 0, 2], [4, 5, 2, 0, 0, 0])
]

count: int = 0

for nums, expected in test_cases:
    move_zeroes(nums)

    actual = nums

    print("Expected:", expected)
    print("Actual:  ", actual)
    print("Result:  ", "PASS" if actual == expected else "FAIL")
    print()

    if actual == expected:
        count += 1

print(f'{count}/{5} PASSED')
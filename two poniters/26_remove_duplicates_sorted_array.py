"""

leetcode 26
remove duplicated from sorted array

"""


def remove_duplicates(nums):
    n = len(nums)
    left = 0
    right=1

    for right in range(n):
        if nums[left] != nums[right]:
            left+=1
            temp = nums[left]
            nums[left] = nums[right]
            nums[right]=temp
            
    
    return left+1



# Main code

test_cases = [
    ([1, 1, 2], 2, [1, 2]),
    ([0, 0, 1, 1, 2, 2, 3], 4, [0, 1, 2, 3]),
    ([1, 2, 3], 3, [1, 2, 3]),
    ([1, 1, 1, 1], 1, [1]),
    ([-3, -3, -1, 0, 0, 2], 4, [-3, -1, 0, 2])
]



count: int = 0

for nums, expected_k, expected_arr in test_cases:
    actual_k = remove_duplicates(nums)

    actual_arr = nums[:actual_k]

    print("Input:   ", nums)
    print("Expected:", expected_k, expected_arr)
    print("Actual:  ", actual_k, actual_arr)
    print(
        "Result:  ",
        "PASS" if actual_k == expected_k and actual_arr == expected_arr else "FAIL"
    )
    print()

    if actual_k == expected_k and actual_arr == expected_arr:
        count += 1

print(f'{count}/{5} PASSED')
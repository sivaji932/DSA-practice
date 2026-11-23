"""
LeetCode 713 — Subarray Product Less Than K

Given an array of positive integers nums and an integer k, return the number 
of contiguous subarrays whose product is strictly less than k.
"""



def numSubarrayProductLessThanK(nums, k):
    #brute force method O(n^2) TC
    # n = len(nums)
    # count = 0

    # for i in range(n):
    #     product = 1
    #     for j in range(i,n):
    #         product *= nums[j]
    #         if product < k:
    #             count += 1
    #         else:
    #             break
    
    # return count

    # optimal approach - Sliding window
    if k <= 1:
        return 0
    
    n = len(nums)
    left = 0
    right = 0
    count = 0
    product = 1

    for right in range(n):
        product *=  nums[right]
        while product >= k:
            product //= nums[left]
            left += 1

        count+= (right - left + 1)

    return count


# Main code
test_cases = [
    ([10, 5, 2, 6], 100, 8),
    ([1, 2, 3], 0, 0),
    ([1, 1, 1], 2, 6),  #1,11,111  1,11 1
    ([1, 2, 3, 4], 10, 7),
    ([5], 5, 0)       # edge case: product must be STRICTLY less
]

count: int = 0

for nums, k, expected in test_cases:
    actual = numSubarrayProductLessThanK(nums, k)

    print("Input:   ", nums)
    print("K:       ", k)
    print("Expected:", expected)
    print("Actual:  ", actual)
    print("Result:  ", "PASS" if actual == expected else "FAIL")
    print()

    if actual == expected:
        count += 1

print(f'{count}/{5} PASSED')
"""
LeetCode 523 — Continuous Subarray Sum - Medium (sliding window can't solve this problem)


Continuous Subarray Sum asks you to determine whether an array contains a continuous
subarray of length at least 2 whose sum is a multiple of k.

1. Problem description
You are given an integer array nums and an integer k.
Return True if there exists a contiguous subarray that:
1. Contains at least 2 elements.
2. Has a sum divisible by k, meaning sum % k == 0.
Otherwise, return False.



do not update an existing remainder's index. Keeping the earliest index gives the longest possible subarray,
 making it easier to satisfy the required length >= 2.
"""


""" 
SA with multiple of k + SA with non multiple of k = same remainder multiple times
"""


def checkSubarraySum(nums, k):
    #brute force TC O(n^2), SC O(1)
    # n=len(nums)
    
    # for i in range(n):
    #     tot=0
    #     for j in range(i,n):
    #         tot+=nums[j]
    #         if tot%k ==0 and j-i+1 >=2:
    #             return True
            
    # return False


    prefix_sum : int = 0

    #     remainder : index
    d = { 0         :    -1 }  #-1 endukante to find window length correctly when 0 rem found at index 1

    for i in range(len(nums)):
        prefix_sum += nums[i]
        rem = prefix_sum % k
        if rem in d:
            if i - d[rem] >= 2:
                return True
        else:
            d[rem] = i

    return False



# Main code
test_cases = [
    ([23, 2, 4, 6, 7], 6, True),
    ([23, 2, 6, 4, 7], 6, True),
    ([23, 2, 6, 4, 7], 13, False),
    ([5, 0, 0, 0], 3, True),       # tricky
    ([1, 2, 3], 5, True)
]

count: int = 0

for nums, k, expected in test_cases:
    actual = checkSubarraySum(nums, k)

    print("Input:   ", nums)
    print("K:       ", k)
    print("Expected:", expected)
    print("Actual:  ", actual)
    print("Result:  ", "PASS" if actual == expected else "FAIL")
    print()

    if actual == expected:
        count += 1

print(f'{count}/{5} PASSED')
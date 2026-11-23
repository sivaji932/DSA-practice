""" 
LeetCode 1749 — Maximum Absolute Sum of Any Subarray

1. Problem explanation
Given an integer array nums, find the maximum absolute sum of any non-empty contiguous subarray.


In simple terms, find:
- The maximum positive subarray sum.
- The minimum (most negative) subarray sum.
- Return the larger absolute value.

"""


def maxAbsoluteSum(nums):
    # #brute force TC O(n^2) ,SC O(1)
    # n=len(nums)
    # max_sum=0
    
    # for i in range(n):
    #     curr_sum=0
    #     for j in range(i,n):
    #         curr_sum+=nums[j]
    #         max_sum=max(max_sum,abs(curr_sum))
            
    # return max_sum
    
    #optimal approach TC O(n), SC O(1)
    n=len(nums)
    max_sum_so_far=0
    global_max=0
    min_sum_so_far=0
    global_min=0
    
    
    #both gloab min val and global max values have different subarrays
    #either the answer found in +ve or min -ve value (convert to abs value later) that's why we're computing 2 possible ways
    for i in range(n):
        max_sum_so_far=max(nums[i],max_sum_so_far+nums[i])
        global_max=max(global_max,max_sum_so_far)
        
        min_sum_so_far=min(nums[i],min_sum_so_far+nums[i])
        global_min=min(global_min,min_sum_so_far)
        
    return max(global_max,abs(global_min))
            

test_cases = [
    ([1, -3, 2, 3, -4], 5),
    ([2, -5, 1, -4, 3, -2], 8),
    ([1, 2, 3, 4], 10),
    ([-1, -2, -3], 6),
    ([0, 0, 0], 0)
]

count: int = 0

for nums, expected in test_cases:
    actual = maxAbsoluteSum(nums)
    status = "PASS" if actual == expected else "FAIL"

    print(f"{status}: expected={expected}, actual={actual}")

    if actual == expected:
        count += 1

print(f"{count}/5 PASSED")


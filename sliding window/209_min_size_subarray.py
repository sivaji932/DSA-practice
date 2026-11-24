"""

LeetCode 209 Minimum Size Subarray Sum
Difficulty: Medium

Problem: Given an array of positive integers nums and a positive integer target,
return the minimal length of a contiguous subarray whose sum is greater than or equal
to target.

If no such subarray exists, return 0.

"""

def minSubArrayLen(target, nums):
    #brute force TC O(n^2), SC O(1)
    # n=len(nums)
    # min_window=float('inf')
    
    # for i in range(n):
    #     tot=0
    #     for j in range(i,n):
    #         tot+=nums[j]
    #         if tot>=target:
    #             min_window=min(min_window,j-i+1)
    #     tot=0
        
    # return min_window if min_window != float('inf') else 0
    
    #sliding window TC O(n), SC O(1)
    n=len(nums)
    left=0
    min_window=float('inf')
    tot=0
    
    for right in range(n):
        tot+=nums[right]
        
        while tot>=target:
            min_window=min(min_window,right-left+1)
            tot-=nums[left]
            left+=1
            
    return min_window if min_window != float('inf') else 0


test_cases = [
    (7, [2, 3, 1, 2, 4, 3], 2),
    (4, [1, 4, 4], 1),
    (11, [1, 1, 1, 1, 1, 1, 1, 1], 0),
    (15, [1, 2, 3, 4, 5], 5),
    (6, [10, 2, 3], 1),
]

passed = 0

for i, (target, nums, expected) in enumerate(test_cases, 1):
    actual = minSubArrayLen(target, nums)

    if actual == expected:
        print(f"Test Case {i}: PASSED")
        passed += 1
    else:
        print(f"Test Case {i}: FAILED | Expected: {expected}, Got: {actual}")

print(f"\n{passed}/{len(test_cases)} PASSED")
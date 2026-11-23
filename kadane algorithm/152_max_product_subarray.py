"""

LeetCode 152 — Maximum Product Subarray

Pattern: Dynamic Programming / Kadane’s Algorithm Variation
1. Problem explanation
Given an integer array nums, find the contiguous subarray with the largest product and return that product.

Remember: multiplying two negative numbers produces a positive number. 
So, we must track both the maximum and minimum products ending at each position.

"""


def maxProduct(nums):
    #brute force TC O(n^2), SC O(1)
    # n=len(nums)
    # if n==1:
    #     return nums[0]
    
    # max_prod=0
    
    # for i in range(n):
    #     curr_prod=1
    #     for j in range(i,n):
    #         curr_prod*=nums[j]
    #         max_prod=max(max_prod,curr_prod)
            
    # return max_prod
    
    
    #optimal appraoch TC O(n), SC O(1)
    n=len(nums)
    prefix_prod=1
    suffix_prod=1
    max_prod=float('-inf')
    
    #negtive value front and back side subarrays product lo max choose chei
    #one pass lone both prefix and suffix products calculate chei
    #0 vasthe 1 ki reset chei
    
    for i in range(n):
        if prefix_prod==0:
            prefix_prod=1
        if suffix_prod==0:
            suffix_prod=1
        
        prefix_prod*=nums[i]
        suffix_prod*=nums[n-i-1]
        
        max_prod=max(max_prod,prefix_prod,suffix_prod)
        
    return max_prod
    
    

#driver code
test_cases = [
    ([2, 3, -2, 4], 6),
    ([-2, 0, -1], 0),
    ([-2, 3, -4], 24),
    ([-2], -2),
    ([0, 2], 2)
]

count: int = 0

for nums, expected in test_cases:
    actual = maxProduct(nums)
    status = "PASS" if actual == expected else "FAIL"

    print(f"{status}: expected={expected}, actual={actual}")

    if actual == expected:
        count += 1

print(f"{count}/5 PASSED")

"""
LeetCode 1004: Max Consecutive Ones III
1. Problem
Given a binary array nums and an integer k, find the maximum number of consecutive 
1s you can get by flipping at most k zeros into ones.

"""



def longestOnes(nums, k):
    # Your code here
    # n=len(nums)
    # left=0
    # right=0
    # max_window=0
    # zeroes=0
    
    # for right in range(n):
    #     if nums[right]==0:
    #         zeroes+=1
            
    #     while zeroes>k:
    #         if nums[left]==0:
    #             zeroes-=1
    #         left+=1
            
    #     max_window= max(max_window,(right-left)+1)
        
    # return max_window
    
    n=len(nums)
    left=0
    right=0
    max_window=0
    zeroes=0
    
    for right in range(n):
        if nums[right]==0:
            zeroes+=1
            
        if zeroes>k:
            if nums[left]==0:
                zeroes-=1
            left+=1
           
        if zeroes<=k: 
            max_window= max(max_window,(right-left)+1)
        
    return max_window



test_cases = [
    ([1, 1, 0, 0, 1, 1, 1, 0, 1], 2, 7),
    ([1, 1, 1, 1], 2, 4),
    ([0, 0, 0, 0], 2, 2),
    ([1, 0, 1, 1, 0, 1], 1, 4),
    ([0, 0, 1, 1, 1, 0, 1], 0, 3)
]

count: int = 0

for nums, k, expected in test_cases:
    actual = longestOnes(nums, k)
    status = "PASS" if actual == expected else "FAIL"

    print(f"{status}: expected={expected}, actual={actual}")

    if actual == expected:
        count += 1

print(f"{count}/5 PASSED")

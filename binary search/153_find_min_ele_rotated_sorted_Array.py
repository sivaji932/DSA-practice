"""
LeetCode 153 – Find Minimum in Rotated Sorted Array
Difficulty: Medium

Problem: Given an array of unique elements originally sorted in ascending order 
and rotated between 1 and n times, find the minimum element.
"""


def findMin(nums):
    #binary search TC O(log n), SC O(1)
    n=len(nums)
    low=0
    high=n-1
    mini=float('inf')
    
    while low<=high:
        mid=low+(high-low)//2
        
        if nums[low]<=nums[mid]:
            mini=min(mini,nums[low])
            low=mid+1
        else:
            mini=min(mini,nums[mid])
            high=mid-1
    
    
    return mini
    

test_cases = [
    ([3, 4, 5, 1, 2], 1),
    ([4, 5, 6, 7, 0, 1, 2], 0),
    ([11, 13, 15, 17], 11),
    ([2, 1], 1),
    ([5, 1, 2, 3, 4], 1),
]

passed = 0

for i, (nums, expected) in enumerate(test_cases, 1):
    actual = findMin(nums)

    if actual == expected:
        print(f"Test Case {i}: PASSED")
        passed += 1
    else:
        print(f"Test Case {i}: FAILED | Expected: {expected}, Got: {actual}")

print(f"\n{passed}/{len(test_cases)} PASSED")
"""
LeetCode 34 Find First and Last Position of Element in Sorted Array
Difficulty: Medium

Problem: Given an array of integers nums sorted in non-decreasing order, 
         find the starting and ending position of a given target value.

If the target is not found, return [-1, -1].

"""
def find_first_pos(nums,target):
    n=len(nums)
    low=0
    high=n-1
    first=-1
    
    while low<=high:
        mid=low+(high-low)//2
        if nums[mid]==target:
            first=mid
            high=mid-1
        elif nums[mid]<target:
            low=mid+1
        else:
            high=mid-1
            
    return first

def find_last_pos(nums,target):
    n=len(nums)
    low=0
    high=n-1
    last=-1
    
    while low<=high:
        mid=low+(high-low)//2
        if nums[mid]==target:
            last=mid
            low=mid+1
        elif nums[mid]<target:
            low=mid+1
        else:
            high=mid-1 
            
    return last


def searchRange(nums, target):
    if len(nums)<1:
        return [-1, -1]
    
    #brute force TC O(n), SC O(1)
    # n=len(nums)
    # first=-1
    # last=-1
    
    # for i in range(n):
    #     if nums[i]==target:
    #         if first==-1:
    #             first=i
    #         last=i
    
    return [find_first_pos(nums,target),find_last_pos(nums,target)]

test_cases = [
    ([5, 7, 7, 8, 8, 10], 8, [3, 4]),
    ([5, 7, 7, 8, 8, 10], 6, [-1, -1]),
    ([], 0, [-1, -1]),
    ([1], 1, [0, 0]),
    ([2, 2, 2, 2, 2], 2, [0, 4]),
]

passed = 0

for i, (nums, target, expected) in enumerate(test_cases, 1):
    actual = searchRange(nums, target)

    if actual == expected:
        print(f"Test Case {i}: PASSED")
        passed += 1
    else:
        print(f"Test Case {i}: FAILED | Expected: {expected}, Got: {actual}")

print(f"\n{passed}/{len(test_cases)} PASSED")
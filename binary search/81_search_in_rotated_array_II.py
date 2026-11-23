"""
LeetCode 81 – Search in Rotated Sorted Array II
Difficulty: Medium

Problem: Given an integer array nums sorted in non-decreasing order and rotated at an unknown pivot, search for a given target.

Return True if the target exists in the array; otherwise, return False.

Note: The array may contain duplicates.

similar to leetcode 33 but with one modification to handle edge case of duplicates

"""


def search(nums, target):
    #binary search TC-O(n/2) in worst case, SC O(1)
    n=len(nums)
    low=0
    high=n-1
    ans=False
    
    while low<=high:
        mid=low+(high-low)//2
        if nums[mid]==target:
            ans=True
            break
        
        if nums[low]==nums[mid]==nums[high]:
            low+=1
            high-=1
            continue
        
        if nums[low]<=nums[mid]:
            if nums[low]<=target and target<=nums[mid]:
                high=mid-1
            else:
                low=mid+1
        else:
            if nums[mid]<=target and target<=nums[high]:
                low=mid+1
            else:
                high=mid-1
                
    return ans

test_cases = [
    ([2, 5, 6, 0, 0, 1, 2], 0, True),
    ([2, 5, 6, 0, 0, 1, 2], 3, False),
    ([1, 0, 1, 1, 1], 0, True),
    ([1, 1, 1, 1, 1], 1, True),
    ([3, 1], 1, True),
]

passed = 0

for i, (nums, target, expected) in enumerate(test_cases, 1):
    actual = search(nums, target)

    if actual == expected:
        print(f"Test Case {i}: PASSED")
        passed += 1
    else:
        print(f"Test Case {i}: FAILED | Expected: {expected}, Got: {actual}")

print(f"\n{passed}/{len(test_cases)} PASSED")
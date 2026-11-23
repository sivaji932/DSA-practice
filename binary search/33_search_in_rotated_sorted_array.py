"""

LeetCode 33 – Search in Rotated Sorted Array
Difficulty: Medium

Problem: Given an integer array nums sorted in ascending order and then rotated 
         at an unknown pivot, search for a given target.

Return the index of target if it exists; otherwise, return -1.

"""

def search(nums, target):
    #linear search TC O(n), SC O(1)
    # n=len(nums)
    # ans=-1
    
    # for i in range(n):
    #     if nums[i]==target:
    #         ans=i
    #         break
    
    # return ans
    
    
    # binary search TC O(log n), SC O(1)
    n=len(nums)
    ans=-1
    low=0
    high=n-1
    
    while low<=high:
        mid=low+(high-low)//2
        if nums[mid]==target:
            ans=mid
            break
        
        #the 2 main steps
        # 1) identify the sorted half
        # 2) check target bound
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
    ([4, 5, 6, 7, 0, 1, 2], 0, 4),
    ([4, 5, 6, 7, 0, 1, 2], 3, -1),
    ([1], 0, -1),
    ([1], 1, 0),
    ([3, 1], 1, 1),
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
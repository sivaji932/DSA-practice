"""

Problem: Given a sorted array of distinct integers and a target value, 
return the index if the target is found. If not, return the index where it would be inserted in order.

"""


def searchInsert(nums, target):
    #brute force TC O(n), SC SC O(1)
    # n=len(nums)
    # ans=n
    
    # for i in range(n):
    #     if nums[i]>=target:
    #         ans=i
    #         return ans
        
    # return ans
    
    #optimal apppraoch binary search TC O(log n), SC O(1)
    n=len(nums)
    low=0
    high=n-1
    ans=n
    
    while low<=high:
        mid= low+(high-low)//2
        if nums[mid]>=target:
            ans=mid
            high=mid-1
        else:
            low=mid+1
            
    return ans



test_cases = [
    ([1, 3, 5, 6], 5, 2),
    ([1, 3, 5, 6], 2, 1),
    ([1, 3, 5, 6], 7, 4),
    ([1, 3, 5, 6], 0, 0),
    ([1], 0, 0),
]

passed = 0

for i, (nums, target, expected) in enumerate(test_cases, 1):
    actual = searchInsert(nums, target)

    if actual == expected:
        print(f"Test Case {i}: PASSED")
        passed += 1
    else:
        print(f"Test Case {i}: FAILED | Expected: {expected}, Got: {actual}")

print(f"\n{passed}/{len(test_cases)} PASSED")
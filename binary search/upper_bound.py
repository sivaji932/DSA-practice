"""

Upper Bound
Given a sorted array arr[] and a number target, find the upper bound of the target 
in this given array. The upper bound of a number is defined as the smallest index 
in the sorted array where the element is greater than the given number.

Note: If all the elements in the given array are smaller than or equal to the target,
      the upper bound will be the length of the array.

Examples:

Input: arr[] = [2, 3, 7, 10, 11, 11, 25], target = 9
Output: 3
Explanation: 3 is the smallest index in arr[] at which element (arr[3] = 10) is larger than 9.

Input: arr[] = [2, 3, 7, 10, 11, 11, 25], target = 11
Output: 6
Explanation: 6 is the smallest index in arr[]at which element (arr[6] = 25) is larger than 11.

Input: arr[] = [2, 3, 7, 10, 11, 11, 25], target = 100
Output: 7
Explanation: As no element in arr[]is greater than 100, return the length of array.


"""

def searchInsert(nums, target):
    #brute force TC O(n), TC O(1)
    # n=len(nums)
    # ans=n
    
    # for i in range(n):
    #     if nums[i]>target:
    #         ans=i
    #         return ans
        
    # return ans
    
    #optimal approach binary search TC O(log n), SC O(1)
    n=len(nums)
    low=0
    high=n-1
    ans=n
    
    while low<=high:
        mid=low+(high-low)//2
        if nums[mid]>target:
            ans=mid
            high=mid-1
        else:
            low=mid+1
            
    return ans


test_cases = [
    ([1, 3, 5, 6], 5, 3),
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
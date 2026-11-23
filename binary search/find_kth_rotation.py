"""
GeeksforGeeks – Find Kth Rotation
Problem: Given a sorted array that has been rotated, find the number of times the array has been rotated.

Return the index of the smallest element (minimum element), which represents the number of rotations.
"""

def findKRotation(arr):
    #
    n=len(arr)
    low=0
    high=n-1
    mini=float('inf')
    index=-1
    
    
    while low<=high:
        mid=low+(high-low)//2
        
        if arr[low]<=arr[mid]:
            if arr[low]<mini:
                mini=arr[low]
                index=low
            low=mid+1
        else:
            if arr[mid]<mini:
                mini=arr[mid]
                index=mid
            high=mid-1
            
    return index

test_cases = [
    ([5, 1, 2, 3, 4], 1),
    ([1, 2, 3, 4, 5], 0),
    ([3, 4, 5, 1, 2], 3),
    ([4, 5, 6, 7, 0, 1, 2], 4),
    ([2, 1], 1),
]

passed = 0

for i, (arr, expected) in enumerate(test_cases, 1):
    actual = findKRotation(arr)

    if actual == expected:
        print(f"Test Case {i}: PASSED")
        passed += 1
    else:
        print(f"Test Case {i}: FAILED | Expected: {expected}, Got: {actual}")

print(f"\n{passed}/{len(test_cases)} PASSED")
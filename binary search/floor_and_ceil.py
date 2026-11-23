"""

GeeksforGeeks Floor and Ceil in a Sorted Array
Problem: Given a sorted array arr[] and a target x, find the indexes of:
- Floor: Index of the greatest element smaller than or equal to x. 
- Ceil: Index of the smallest element greater than or equal to x. (ele>=x)
Return [-1, -1] if neither exists.
#[1, 2, 4, 6, 8, 10]

"""


def getFloorAndCeil(arr, n, x):
    #
    low=0
    high=n-1
    floor=-1
    ceil=-1
    
    #floor
    while low<=high:
        mid=low+(high-low)//2
        if arr[mid]<=x:
            floor=mid
            low=mid+1 #becoz we have to right side to find biggest possible value i.e <=x
        else:
            high=mid-1
             
            
    #ceil
    low=0
    high=n-1
    while low<=high:
        mid=low+(high-low)//2
        if arr[mid]>=x:
            ceil=mid
            high=mid-1
        else:
            low=mid+1
        
    
    return [floor,ceil]


test_cases = [
    ([1, 2, 4, 6, 8, 10], 6, 5, (2, 3)),
    ([1, 2, 4, 6, 8, 10], 6, 4, (2, 2)),
    ([1, 2, 4, 6, 8, 10], 6, 0, (-1, 0)),
    ([1, 2, 4, 6, 8, 10], 6, 12, (5, -1)),
    ([2, 5, 8, 12, 16], 5, 10, (2, 3)),
]

passed = 0

for i, (arr, n, x, expected) in enumerate(test_cases, 1):
    actual = getFloorAndCeil(arr, n, x)

    if tuple(actual) == expected:
        print(f"Test Case {i}: PASSED")
        passed += 1
    else:
        print(f"Test Case {i}: FAILED | Expected: {expected}, Got: {actual}")

print(f"\n{passed}/{len(test_cases)} PASSED")
"""

GeeksforGeeks Lower Bound
Problem: Given a sorted array arr[] and an integer x, find the index of the smallest 
element that is greater than or equal to x. If no such element exists, return n.

"""


def lowerBound( arr, n, x):
    #the og brute force appraoch TC O(n), SC O(1)
    # ans=n
    
    # for i in range(n):
    #     if arr[i]>=x:
    #         ans=i
    #         return ans
        
    # return ans
    
    #optimal appraoch binary search TC O(log n), SC O(1)
    ans=n
    low=0
    high=n-1
    
    while low<=high:
        mid=low+(high-low)//2   
        if arr[mid]>=x: 
            ans=mid
            high=mid-1 #as we need to find lowest index possible.
        else:
            low=mid+1
            
    return ans   
        
#driver code
test_cases = [
    ([1, 2, 4, 4, 5, 6], 6, 4, 2),
    ([1, 2, 4, 4, 5, 6], 6, 3, 2),
    ([1, 2, 3, 4, 5], 5, 1, 0),
    ([1, 2, 3, 4, 5], 5, 6, 5),
    ([2, 3, 5, 7, 9], 5, 5, 2),
]

passed = 0

for i, (arr, n, x, expected) in enumerate(test_cases, 1):
    actual = lowerBound(arr, n, x)

    if actual == expected:
        print(f"Test Case {i}: PASSED")
        passed += 1
    else:
        print(f"Test Case {i}: FAILED | Expected: {expected}, Got: {actual}")

print(f"\n{passed}/{len(test_cases)} PASSED")

"""
Binary search

"""

def binary_search(arr,target):
    n=len(arr)
    low=0
    high=n-1
    
    while low <= high:
        mid= (low+high)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            low=mid+1
        elif arr[mid]>target:
            high=mid-1
    
    return -1

    


test_cases = [
    ([1, 3, 5, 7, 9], 5, 2),
    ([2, 4, 6, 8, 10], 10, 4),
    ([1, 2, 3, 4, 5], 1, 0),
    ([1, 3, 5, 7, 9], 4, -1),
    ([], 10, -1)
]

count: int = 0

for arr, target, expected in test_cases:
    actual1 = binary_search(arr, target)

    status = "PASS" if actual1 == expected else "FAIL"

    print(f"{status}: expected={expected}, iterative={actual1}")

    if status == "PASS":
        count += 1

print(f"{count}/5 PASSED")

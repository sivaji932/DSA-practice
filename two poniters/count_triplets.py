"""
Count Triplets — Basic Two-Pointer Version
"""

#NOT XOMPLETED

def count_triplets(arr, target):
    n = len(arr)
    fixed=0
    count=0

    for fixed in range(n-2):
        left=fixed+1
        right=n-1

        while left<right:
            triplet_sum= arr[fixed]+arr[left]+arr[right]
            if triplet_sum == target:
                count+=1
                left+=1
                right-=1
            elif triplet_sum > target:
                right-=1
            else:
                left+=1
    
    return count


# Main code

#print(count_triplets([1, 1, 1, 1]))
test_cases = [
    ([1, 2, 3, 4, 5], 9, 2),
    ([1, 1, 1, 1], 3, 4),
    ([2, 4, 6, 8], 20, 1),
    ([1, 2, 2, 3, 4], 7, 3),
    ([-2, -1, 0, 1, 2, 3], 0, 3)
]

count: int = 0

for arr, target, expected in test_cases:
    actual = count_triplets(arr, target)

    print("Input:   ", arr)
    print("Target:  ", target)
    print("Expected:", expected)
    print("Actual:  ", actual)
    print("Result:  ", "PASS" if actual == expected else "FAIL")
    print()

    if actual == expected:
        count += 1

print(f'{count}/{5} PASSED')
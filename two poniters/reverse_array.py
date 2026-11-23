"""
 reverse an array in place using two pointers
"""

def reverse_array(arr):
    if arr is []:
        return []
    n= len(arr)
    left=0
    right =n-1

    while left < right:
        temp = arr[left]
        arr[left]=arr[right]
        arr[right]=temp

        left += 1
        right -=1

    return arr


# Main code
test_cases = [
    ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
    ([1, 2], [2, 1]),
    ([1], [1]),
    ([], []),
    ([-1, 2, -3, 4], [4, -3, 2, -1])
]

count: int = 0

for arr, expected in test_cases:
    actual = reverse_array(arr)

    print("Input:   ", arr)
    print("Expected:", expected)
    print("Actual:  ", actual)
    print("Result:  ", "PASS" if actual == expected else "FAIL")
    print()

    if actual == expected:
        count += 1

print(f'{count}/{5} PASSED')

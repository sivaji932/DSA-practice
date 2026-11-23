"""

two sum sorted array using two pointers

"""



def two_sum_sorted(arr, target):
    n= len(arr)
    left = 0
    right = n-1

    while left < right:
        s = arr[left] + arr[right]
        if s == target:
            return [left,right]
        elif s > target:
            right -= 1
        else:
            left +=1

    return None


# Main code
test_cases = [
    ([1, 2, 3, 4, 6], 6, [1, 3]),
    ([2, 3, 4, 8], 10, [0, 3]),
    ([1, 3, 5, 7], 20, None),
    ([1, 2], 3, [0, 1]),
    ([1, 1, 2, 3, 4], 2, [0, 1])
]

count: int = 0

for arr, target, expected in test_cases:
    actual = two_sum_sorted(arr, target)

    print("Input:   ", arr)
    print("Target:  ", target)
    print("Expected:", expected)
    print("Actual:  ", actual)
    print("Result:  ", "PASS" if actual == expected else "FAIL")
    print()

    if actual == expected:
        count += 1

print(f'{count}/{5} PASSED')
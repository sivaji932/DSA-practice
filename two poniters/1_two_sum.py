"""
two sum 1 
"""


def two_sum(arr, target):
    n = len(arr)
    d = {}

    for i in range(n):
        need = target - arr[i]
        if need in d:
            return [d[need],i]
        else:
            d[arr[i]] = i

    return []


# Main code
test_cases = [
    ([2, 7, 11, 15], 9, [0, 1]),
    ([2, -3, 5, 7], 4, [1, 3]),
    ([3, 3], 6, [0, 1]),
    ([-1, -2, -3, -4, -5], -8, [2, 4]),
    ([0, 4, 3, 0], 0, [0, 3])
]

count: int = 0

for arr, target, expected in test_cases:
    actual = two_sum(arr, target)

    print("Input:   ", arr)
    print("Target:  ", target)
    print("Expected:", expected)
    print("Actual:  ", actual)
    print("Result:  ", "PASS" if actual == expected else "FAIL")
    print()

    if actual == expected:
        count += 1

print(f'{count}/{5} PASSED')
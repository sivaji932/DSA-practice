"""
    find which subarray has max sum

    kadane's algorith extension

    intution:
        recall the kadane's algo and remember
        whenever current array ele > current sum just update the respective variables.
"""


def max_subarray(arr):
    max_sum_so_far : int = arr[0]
    curr_sum :int = arr[0]
    start : int = 0
    end : int = 0
    n : int = len(arr)
    temp_start :int = 0


    for i in range(1,n):
        if arr[i] > curr_sum + arr[i]:
            temp_start = i
            curr_sum = arr[i]
        else:
            curr_sum = curr_sum + arr[i]

        if curr_sum > max_sum_so_far:
            max_sum_so_far = curr_sum
            start = temp_start
            end = i


    return (arr[start:end+1],max_sum_so_far)



# Main code
test_cases = [
    ([-2, 3, -1, 5, -6, 4, 2], ([3, -1, 5], 7)),
    ([1, 2, 3, 4], ([1, 2, 3, 4], 10)),
    ([-5, -2, -8, -1], ([-1], -1)),
    ([4, -1, 2, 1, -5, 4], ([4, -1, 2, 1], 6)),
    ([-2, 1, -3, 4, -1, 2, 1], ([4, -1, 2, 1], 6))
]

count: int = 0

for arr, expected in test_cases:
    actual = max_subarray(arr)

    print("Input:   ", arr)
    print("Expected:", expected)
    print("Actual:  ", actual)
    print("Result:  ", "PASS" if actual == expected else "FAIL")
    print()

    if actual == expected:
        count += 1

print(f'{count}/{5} PASSED')
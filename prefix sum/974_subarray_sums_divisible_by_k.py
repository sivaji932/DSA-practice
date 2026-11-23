"""
Given an integer array nums and integer k, return the number of non-empty 
contiguous subarrays whose sum is divisible by k.
"""


def subarraysDivByK(nums, k):
    #brute force

    # count = 0
    # n = len(nums)

    # for i in range(n):
    #     for j in range(i+1,n+1):
    #         if sum(nums[i:j]) % k == 0:
    #             count += 1

    # return count

    # optimal approach with prefix sum
    #     Rem : Freq 
    d = { 0  :   1 }
    n = len(nums)
    prefix_sum = 0
    count = 0

    for i in range(n):
        prefix_sum += nums[i]
        rem = prefix_sum % k
        # if rem < 0:
        #     rem += k
        
        if rem in d:
            count+=d[rem]
            d[rem] += 1
        else:
            d[rem] = 1

    return count


# Main code
test_cases = [

    ([4, 5, 0, -2, -3, 1], 5, 7),
    ([5], 5, 1),
    ([1, 2, 3], 3, 3),
    ([-1, 2, 9], 2, 2),
    ([0, 0, 0, 0], 1, 10)   # tricky: every subarray is valid
]

count: int = 0

for nums, k, expected in test_cases:
    actual = subarraysDivByK(nums, k)

    print("Input:   ", nums)
    print("K:       ", k)
    print("Expected:", expected)
    print("Actual:  ", actual)
    print("Result:  ", "PASS" if actual == expected else "FAIL")
    print()

    if actual == expected:
        count += 1

print(f'{count}/{5} PASSED')
"""
leetcode 560 
Count Subarrays with Sum K

Given an array and a target K, find how many contiguous subarrays have a sum exactly equal to K.
"""


""" 
Sa with sum =k + SA with sum !=k = prefix sum at that index
"""

def count_subarrays(arr, k):
    #brute force O(n^2)

    # count : int  = 0

    # n : int  = len(arr)
    # for i in range(n):
    #     for j in range(i+1,n+1):
    #         if sum(arr[i:j]) == k:
    #             count += 1

    # return count


    # prefix sum method O(n)

    #             sum : freq   
    prefix_sum = { 0   :  1 } 
    # 1 endukante, to handle the case where a subarray starting from very beginning sums upto exactly k
    #okavela 0 pedithe starting lo kanaka valid subarray unte miss count avudhi eg [3,4] k=3

    """
    why the above dict?
    - to cover the pending possibilities as the prefixsum tracing wont give full answer
    - if prefix sum - k in dict there is a possibility to form subarray of sum k (avoid the left sub array from that index)

    """

    n : int = len(arr)
    count : int = 0
    tot_sum : int  = 0 # to track max sum so far means prefix sum variable

    for i in range(n):  #only single pass
        tot_sum += arr[i]
        if (tot_sum - k) in prefix_sum:
            count += prefix_sum[tot_sum - k] #carefully update with only found value


        if tot_sum in prefix_sum:
            prefix_sum[tot_sum] += 1  #update the freq 
        else:
            prefix_sum[tot_sum] = 1 # insert new if the sum is not present

    return count


# Main code
test_cases = [
    ([1, 1, 1], 2, 2),
    ([1, 2, 3], 3, 2),
    ([1, -1, 1, -1], 0, 4),
    ([3, 4, 7, 2, -3, 1, 4, 2], 7, 4),
    ([5, -2, 3, 1, 2], 3, 3)   # tricky case
]

count: int = 0

for arr, k, expected in test_cases:
    actual = count_subarrays(arr, k)

    print("Input:   ", arr)
    print("K:       ", k)
    print("Expected:", expected)
    print("Actual:  ", actual)
    print("Result:  ", "PASS" if actual == expected else "FAIL")
    print()

    if actual == expected:
        count += 1

print(f'{count}/{5} PASSED')
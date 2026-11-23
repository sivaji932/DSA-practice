"""
LeetCode 16 — 3Sum Closest
"""


def three_sum_closest(nums, target):
    #brute force O(n^3) TC
    # n=len(nums)
    # closest_sum=0
    # gap=float('inf')

    # for i in range(0,n-1):
    #     for j in range(i+1,n-1):
    #         for k in range(j+1,n):
    #             triplet_sum=nums[i]+nums[j]+nums[k]
    #             if triplet_sum>target:
    #                 if gap>triplet_sum-target:
    #                     gap=triplet_sum-target
    #                     closest_sum=triplet_sum
    #             elif triplet_sum<target:
    #                 if gap>target-triplet_sum:
    #                     gap=target-triplet_sum
    #                     closest_sum=triplet_sum
    #             else:
    #                 return target
    # return closest_sum

    # two pinters 
    n=len(nums)
    nums.sort()
    gap=float('inf')
    closest_sum=0

    for i in range(n-1):
        j=i+1
        k=n-1
        while j<k:
            triplet_sum=nums[i]+nums[j]+nums[k]
            if triplet_sum>target:
                k-=1
                if gap>triplet_sum-target:
                    gap=triplet_sum-target
                    closest_sum=triplet_sum
            elif triplet_sum<target:
                j+=1
                if gap>target-triplet_sum:
                    gap=target-triplet_sum
                    closest_sum=triplet_sum
            else:
                return triplet_sum
        
    return closest_sum


    


# Main code
test_cases = [
    ([-1, 2, 1, -4], 1, 2),
    ([0, 0, 0], 1, 0),
    ([1, 1, 1, 0], 100, 3),
    ([-3, -2, -5, 3, -4], -1, -2),
    ([1, 2, 4, 8, 16, 32], 15, 14)
]

count: int = 0

for nums, target, expected in test_cases:
    actual = three_sum_closest(nums, target)

    print("Input:   ", nums)
    print("Target:  ", target)
    print("Expected:", expected)
    print("Actual:  ", actual)
    print("Result:  ", "PASS" if actual == expected else "FAIL")
    print()

    if actual == expected:
        count += 1

print(f'{count}/{5} PASSED')
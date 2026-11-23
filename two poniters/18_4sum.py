"""
LeetCode 18 — 4Sum
"""

def four_sum(nums, target):
    #brute force O(n^4) TC and O(qudraplets) SC
    # n=len(nums)
    # res=set()

    # for a in range(n-3):
    #     for b in range(a+1,n-2):
    #         for c in range(b+1,n-1):
    #             for d in range(c+1,n):
    #                 quadraplets_sum=nums[a]+nums[b]+nums[c]+nums[d]
    #                 if quadraplets_sum==target:
    #                     quadraplets= tuple(sorted([nums[a],nums[b],nums[c],nums[d]]))
    #                     res.add(quadraplets)

    # return [list(q) for q in res ]

    #better approach with two pointers O(n)
    nums.sort()
    n=len(nums)
    res=[]

    for i in range(n-3):
        if i>0 and nums[i-1]==nums[i]:
            continue
        
        for j in range(i+1,n-2):
            if j>i+1 and nums[j-1]==nums[j]:
                continue
                
            k=j+1
            l=n-1
            while k<l:
                quadraplets_sum=nums[i]+nums[j]+nums[k]+nums[l]
                if quadraplets_sum==target:
                    res.append([nums[i],nums[j],nums[k],nums[l]])
                    k+=1
                    l-=1

                    while k<l and nums[k-1]==nums[k]:
                        k+=1
                    while k<l and nums[l+1]==nums[l]:
                        l-=1
                
                elif quadraplets_sum>target:
                    l-=1
                else:
                    k+=1
                
    return res


# Main code
test_cases = [
    (
        [1, 0, -1, 0, -2, 2],
        0,
        [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
    ),
    ([2, 2, 2, 2, 2], 8, [[2, 2, 2, 2]]),
    ([1, 2, 3, 4], 10, [[1, 2, 3, 4]]),
    ([1, 2, 3, 4], 100, []),
    ([-3, -1, 0, 2, 4, 5], 2, [[-3, -1, 2, 4]])
]

count: int = 0

for nums, target, expected in test_cases:
    actual = four_sum(nums, target)

    # Sort quadruplets so output ordering doesn't affect comparison
    actual = sorted([sorted(q) for q in actual])
    expected = sorted([sorted(q) for q in expected])

    print("Input:   ", nums)
    print("Target:  ", target)
    print("Expected:", expected)
    print("Actual:  ", actual)
    print("Result:  ", "PASS" if actual == expected else "FAIL")
    print()

    if actual == expected:
        count += 1

print(f'{count}/{5} PASSED')
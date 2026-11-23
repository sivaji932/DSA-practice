"""
LeetCode 15 — 3Sum
"""


def three_sum(nums):
    # brute force O(n^2)
    # n=len(nums)
    # ans=set()

    # for i in range(n):
    #     for j in range(i+1,n):
    #         for k in range(j+1,n):
    #             if (nums[i]+nums[j]+nums[k])==0:
    #                 triplet=tuple(sorted([nums[i],nums[j],nums[k]]))
    #                 ans.add(triplet)

    # return [list(t) for t in ans]

    #better approach O(n^2) TC + O(triplets) SC along with contant set inside loop 
    # n=len(nums)
    # res=set()

    # for i in range(n-1):
    #     search_space=set()
    #     for j in range(i+1,n):
    #         k=-(nums[i]+nums[j])
    #         if k in search_space:
    #             triplet=tuple(sorted([nums[i],nums[j],k]))
    #             res.add(triplet)
    #         search_space.add(nums[j])

    # print(res)
    # return [list(t) for t in res]


    #optimal approach with Two pointers
    # TC - O(n^2) and SC - O(triplets)
    n=len(nums)
    res=[]

    nums.sort()

    for i in range(0,n-1):
        if i>0 and nums[i-1]==nums[i]:
            i+=1
        j=i+1
        k=n-1
        while j<k:
            triplet_sum=nums[i]+nums[j]+nums[k]
            if triplet_sum==0:
                res.append([nums[i],nums[j],nums[k]])
                j+=1
                k-=1

                while j<k and nums[j-1]==nums[j]:
                    j+=1
                while j<k and nums[k+1]==nums[k]:
                    k-=1
            elif triplet_sum>0:
                k-=1
            else:
                j+=1

    return res


# Main code
test_cases = [
    (
        [-1, 0, 1, 2, -1, -4],
        [[-1, -1, 2], [-1, 0, 1]]
    ),
    (
        [0, 1, 1],
        []
    ),
    (
        [0, 0, 0],
        [[0, 0, 0]]
    ),
    (
        [-2, 0, 1, 1, 2],
        [[-2, 0, 2], [-2, 1, 1]]
    ),
    (
        [-1, -1, -1, 2, 2],
        [[-1, -1, 2]]
    )
]

count: int = 0

for nums, expected in test_cases:
    actual = three_sum(nums)

    # Order of triplets does not matter
    actual = sorted(actual)
    expected = sorted(expected)

    print("Input:   ", nums)
    print("Expected:", expected)
    print("Actual:  ", actual)
    print("Result:  ", "PASS" if actual == expected else "FAIL")
    print()

    if actual == expected:
        count += 1

print(f'{count}/{5} PASSED')
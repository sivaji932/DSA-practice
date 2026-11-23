""""
LeetCode 1480 — Running Sum of 1d Array

"""

def running_sum(nums):
    #brute force TC O(n^2) , SC O(n)
    # n=len(nums)
    # res=[]
    
    # for i in range(n):
    #     csum=0
    #     for j in range(0,i+1):
    #         csum+=nums[j]
    #     res.append(csum)
        
    # return res
    
    #optimal approach TC O(n), SC O(n)
    n=len(nums)
    csum=0
    res=[]
    
    for num in nums:
        csum+=num
        res.append(csum)
        
    return res


test_cases = [
    ([1, 2, 3, 4], [1, 3, 6, 10]),
    ([1, 1, 1, 1, 1], [1, 2, 3, 4, 5]),
    ([3, 1, 2, 10, 1], [3, 4, 6, 16, 17]),
    ([5], [5]),
    ([], [])
]

count: int = 0

for nums, expected in test_cases:
    actual = running_sum(nums)
    status = "PASS" if actual == expected else "FAIL"

    print(f"{status}: expected={expected}, actual={actual}")

    if actual == expected:
        count += 1

print(f"{count}/5 PASSED")

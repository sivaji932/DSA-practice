"""
leetcode pivot index 724

(an extension of range sum 303)


if you write only with loops the time complexity if O(n^2)

but with prefix sum give O(n)
1. First calculate prefixsum
2.iterate through the nums
3.if the first element - to its right subarray is equals (edge case) return 0 
  else calculate & compare the left sum and right sum and do rest

"""


def pivotIndex(nums):
    #brute force TC O(n^2), SC O(1)
    
    # n=len(nums)
    
    # for i in range(n):
    #     left_sum=0
    #     right_sum=0
        
    #     for j in range(0,i):
    #         left_sum+=nums[j]
            
    #     for j in range(i+1,n):
    #         right_sum+=nums[j]
            
    #     if left_sum==right_sum:
    #         return i
        
    # return -1
    
    
    #optimal appraoch TC O(n), SC O(n)
    #calculate prefix sum array

    # prefix_sum = [nums[0]]
    # n = len(nums)

    # for i in range(1,n):
    #     prefix_sum.append(prefix_sum[i-1] + nums[i])

    
    # #traverse the nums to find pivot index
    # for i in range(n):
    #     left_sum = 0 if i == 0 else prefix_sum[i-1]
    #     right_sum =prefix_sum[n-1] - prefix_sum[i]

    #     if left_sum == right_sum:
    #         return i
    
    # return -1
    

    #optimal approach TC O(n), SC O(1)
    
    n=len(nums)
    tot_sum=0
    left_sum=0
    
    for num in nums:
        tot_sum+=num
        
    #first left & right sum compare chesi next left sum ni calculate chei
    for i in range(n):
        if left_sum==tot_sum-left_sum-nums[i]:
            return i
        
        left_sum+=nums[i]
        
    return -1
        

# Main code
test_cases = [
    ([1, 7, 3, 6, 5, 6], 3),
    ([1, 2, 3], -1),
    ([2, 1, -1], 0),
    ([1, -1, 0], 2),       # tricky
    ([0, 0, 0, 0], 0)      # edge case
]

count: int = 0

for nums, expected in test_cases:
    actual = pivotIndex(nums)

    print("Input:   ", nums)
    print("Expected:", expected)
    print("Actual:  ", actual)
    print("Result:  ", "PASS" if actual == expected else "FAIL")
    print()

    if actual == expected:
        count += 1

print(f'{count}/{5} PASSED')
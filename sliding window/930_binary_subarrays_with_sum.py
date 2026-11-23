""""
LeetCode 930 — Binary Subarrays With Sum
Basic explanation
Given a binary array nums (only 0 and 1) and an integer goal, return 
the number of non-empty contiguous subarrays whose sum equals goal.

"""



def numSubarraysWithSum(nums, goal):
    #brute force TC O(n^2) SC O(1)
    # n=len(nums)
    # count=0
    
    # for i in range(n):
    #     sum=0
    #     for j in range(i,n):
    #         sum+=nums[j]
    #         if sum==goal:
    #             count+=1
    #         elif sum>goal:
    #             break
    # return count

    # """
    # Directly applying a sliding window to find subarrays with a sum equal to goal is difficult because 
    # the array contains zeros, which makes window-shrinking ambiguous.To solve this in O(n) time, we use the property:
    
    # Subarrays with Sum = (subarrays with sum <= goal) - (subarrays with sum <= goal-1)
    
    # """
    
    #optimal approach TC O(n) SC O(1)
    def helper(k):
        if k<0:
            return 0
        
        n=len(nums)
        left=0
        right=0
        count=0
        sum=0
        
        for right in range(n):
            sum+=nums[right]
            
            while sum>k:# Shrink window while current sum exceeds k
                sum-=nums[left]
                left+=1
                
            # All subarrays ending at 'right' and starting anywhere from 'left' to 'right' are valid
            count+=(right-left)+1
            
        return count
    
    return helper(goal)-helper(goal-1)


# Main code
test_cases = [
    ([1, 0, 1, 0, 1], 2, 4),
    ([0, 0, 0, 0, 0], 0, 15),
    ([1, 1, 1], 2, 2),
    ([0, 1, 0, 1, 0], 1, 8),
    ([1, 0, 0, 1, 0, 1], 3, 1)
]

count: int = 0

for nums, goal, expected in test_cases:
    actual = numSubarraysWithSum(nums, goal)

    print("Input:   ", nums)
    print("Goal:    ", goal)
    print("Expected:", expected)
    print("Actual:  ", actual)
    print("Result:  ", "PASS" if actual == expected else "FAIL")
    print()

    if actual == expected:
        count += 1

print(f'{count}/{5} PASSED')
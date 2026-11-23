"""

LeetCode 2461 — Maximum Sum of Distinct Subarrays With Length K
Basic explanation
Given an integer array nums and an integer k, find the maximum sum of a subarray of 
length exactly k that contains only distinct elements.

If no valid subarray exists, return 0.

"""


def maximumSubarraySum(nums, k):
    #brute force approach O(n*k) my implementation
    # n=len(nums)
    # if n==1:
    #     return nums[0]
    
    # left=0
    # max_sum=0 
    
    # #calculate every window sum and check if the subbarray has duplicate elements
    # while left<=n-k:
    #     search_window=set()
    #     curr_sum=0
    #     right=left
    #     while right<(left+k): #calculate every k window sum 
    #         if nums[right] in search_window:
    #             curr_sum=0
    #             break
    #         else:
    #             search_window.add(nums[right])
    #             curr_sum+=nums[right]
    #         right+=1
     
    #     if curr_sum>max_sum:
    #         max_sum=curr_sum
    #     left+=1
                               
    # return max_sum
    
    # this approach also TC O(n*k)
    # n=len(nums)
    # if n==1:
    #     return nums[0]
    
    # left=0
    # right=0
    # curr_sum=0
    # max_sum=0
    # search_space=set()
    
    
    # while right<n:
    #     while nums[right] in search_space:
    #         curr_sum-=nums[left]
    #         search_space.remove(nums[left])
    #         left+=1
            
    #     curr_sum+=nums[right]
    #     search_space.add(nums[right])
        
    #     if right-left+1==k:
    #         max_sum=max(curr_sum,max_sum)
    #         search_space.remove(nums[left])
    #         curr_sum-=nums[left]
    #         left+=1
        
    #     right+=1
            
                               
    # return max_sum
    
    #optimal approach TC O(n) and SC O(k)
    n=len(nums)
    if n==1:
        return nums[0]
    
    left=0
    right=0
    curr_sum=0
    max_sum=0
    search_space={}
    
    while right<n:
        curr_sum+=nums[right] #blind ga sum calaculate cheyyi and insert elements or count frequency
        search_space[nums[right]] = search_space.get(nums[right],0) + 1
        
        if right-left+1>k:  #eppudite k window size cross avudho ,left nunchi window narikei
            curr_sum-=nums[left]
            search_space[nums[left]]-=1
            if search_space[nums[left]]==0:
                search_space.pop(nums[left]) # del search_space[nums[left]]
            left+=1
            
        if right-left+1==k and len(search_space)==k:  #if hash map lo k elements and window size k unte max sum check chei
            max_sum=max(curr_sum,max_sum)
            
        right+=1
        
    return max_sum
             

# Main code

test_cases = [
    ([1, 5, 4, 2, 9, 9, 9], 3, 15),
    ([4, 4, 4], 3, 0),
    ([1, 2, 3, 4, 5], 3, 12),
    ([1, 1, 1, 7, 8, 9], 3, 24),
    ([5], 1, 5)
]

count: int = 0

for nums, k, expected in test_cases:
    actual = maximumSubarraySum(nums, k)

    print("Input:   ", nums)
    print("K:       ", k)
    print("Expected:", expected)
    print("Actual:  ", actual)
    print("Result:  ", "PASS" if actual == expected else "FAIL")
    print()

    if actual == expected:
        count += 1

print(f'{count}/{5} PASSED')

"""""
LeetCode 1248 — Count Number of Nice Subarrays

Basic explanation
Given an array of positive integers nums and an integer k, count 
the contiguous subarrays containing exactly k odd numbers.


"""


def numberOfSubarrays(nums, k):
    # Your code here
    #brute force TC O(n^2)
    # n=len(nums)
    # count=0
    
    
    # for i in range(n):
    #     odd_count=0
    #     for j in range(i,n):
    #         if nums[j] % 2 != 0:
    #             odd_count+=1
    #         if odd_count==k:
    #             count+=1
            
    # return count
    
    
    def helper(k): 
        n=len(nums)
        count=0
        left=0
        right=0
        tot=0
        
        
        while right<n:
            tot+=nums[right]%2
            
            while tot>k:
                tot-=nums[left]%2
                left+=1
                
            count+= (right-left)+1
            
            right+=1
            
        return count
    
    return helper(k) - helper(k-1)
        
    

# Main code
test_cases = [
    ([1, 1, 2, 1, 1], 3, 2),
    ([2, 4, 6], 1, 0),
    ([1, 3, 5], 1, 3),
    ([2, 2, 1, 2, 1, 2], 2, 6),   #2, 2, 1, 2, 1   2, 2, 1, 2, 1, 2    2, 1, 2, 1  2, 1, 2, 1, 2    1, 2, 1   1, 2, 1, 2
    ([1], 1, 1)
]

count: int = 0

for nums, k, expected in test_cases:
    actual = numberOfSubarrays(nums, k)

    print("Input:   ", nums)
    print("K:       ", k)
    print("Expected:", expected)
    print("Actual:  ", actual)
    print("Result:  ", "PASS" if actual == expected else "FAIL")
    print()

    if actual == expected:
        count += 1

print(f'{count}/{5} PASSED')
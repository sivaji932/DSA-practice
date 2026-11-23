
"""
Max Consecutive Ones II — LeetCode 487
Basic explanation
Given a binary array, find the maximum number of consecutive 1s if you can flip at most one 0 into a 1.
"""


def findMaxConsecutiveOnes(nums):
    # Your code here
    n=len(nums)
    left=0
    right=0
    max_window=0
    zeroes=0
    
    while right<n:
        if nums[right]==0:
            zeroes+=1
            
        while zeroes>1:
            if nums[left]==0:
                zeroes-=1
                
            left+=1
            
        max_window= max(max_window,(right-left)+1)
        right+=1
        
    return max_window


# Main code
test_cases = [
    ([1, 0, 1, 1, 0], 4),
    ([1, 1, 1, 1], 4),
    ([0, 0, 0], 1),
    ([1, 0, 1, 1, 1, 0, 1], 5),
    ([0], 1)
]

count: int = 0

for nums, expected in test_cases:
    actual = findMaxConsecutiveOnes(nums)

    print("Input:   ", nums)
    print("Expected:", expected)
    print("Actual:  ", actual)
    print("Result:  ", "PASS" if actual == expected else "FAIL")
    print()

    if actual == expected:
        count += 1

print(f'{count}/{5} PASSED')

""""

LeetCode 485 — Max Consecutive Ones I
Basic explanation
Given a binary array containing 0s and 1s, find the maximum number of consecutive 1s.



"""


def findMaxConsecutiveOnes(nums):
    # Your code here
    max_ones=0
    curr_ones=0
    n=len(nums)
    
    for num in nums:
        if num!=0:
            curr_ones+=1
        else:
            curr_ones=0
        
        max_ones=max(max_ones,curr_ones)
            
    return max_ones
            


# Main code
test_cases = [
    ([1, 1, 0, 1, 1, 1], 3),
    ([1, 0, 1, 1, 0], 2),
    ([0, 0, 0], 0),
    ([1, 1, 1, 1], 4),
    ([1], 1)
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
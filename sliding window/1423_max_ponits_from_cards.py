"""

LeetCode 1423 — Maximum Points You Can Obtain from Cards

You are given an array cardPoints and an integer k. You must pick exactly k
cards from either the beginning or the end of the array to maximize the total points.

"""


def maxScore(cardPoints, k):
    # Your code here
    n=len(cardPoints)
    left_sum=0
    right_sum=0
    max_sum=0
    
    #first left sum of window k calculate chei
    for i in range(k):
        left_sum+=cardPoints[i]
        
    max_sum=left_sum
    
    #right window sum inc chesthu left sum dec chei while checking max sum
    #ante left window+sum decrease chesthi right window+sum cheyyali
    right=n-1
    for j in range(k-1,-1,-1):
        left_sum-=cardPoints[j]
        right_sum+=cardPoints[right]
        right-=1
        
        max_sum=max(max_sum,(left_sum+right_sum))
        
    return max_sum
        
        

# Main code
test_cases = [
    ([1, 2, 3, 4, 5, 6, 1], 3, 12),
    ([2, 2, 2], 2, 4),
    ([9, 7, 7, 9, 7, 7, 9], 7, 55),
    ([1, 1000, 1], 1, 1),
    ([1, 79, 80, 1, 1, 1, 200, 1], 3, 202)
]

count: int = 0

for cardPoints, k, expected in test_cases:
    actual = maxScore(cardPoints, k)

    print("Input:   ", cardPoints)
    print("K:       ", k)
    print("Expected:", expected)
    print("Actual:  ", actual)
    print("Result:  ", "PASS" if actual == expected else "FAIL")
    print()

    if actual == expected:
        count += 1

print(f'{count}/{5} PASSED')
"""

LeetCode 875 Koko Eating Bananas
Difficulty: Medium

Problem: Koko loves eating bananas. Given an array piles, where piles[i] represents 
the number of bananas in the ith pile, and an integer h representing the total hours available.

Koko can decide her eating speed k (bananas per hour).
- Each hour, she chooses one pile and eats k bananas from it.
- If the pile has fewer than k bananas, she eats the entire pile.
- She cannot eat from multiple piles in the same hour.
Return the minimum integer eating speed k such that she can finish all bananas within h hours.

"""

from math import ceil

def minEatingSpeed(piles, h):
    #brute force TC - O(max(piles) * n), SC - O(1) ALERT: Absolute time consuming way...
    # n=len(piles)
    # max_eating_count=max(piles)
    # min_eating_count=float('inf') #we have to find
    
    
    # for i in range(1,max_eating_count+1):
    #     tot_time=0
    #     for pile in piles:
    #         curr_pile_time=ceil(pile/i) #to get how many hours to complete one pile
    #         tot_time+=curr_pile_time
    #         if tot_time>h:
    #             # print(f'bananas eating/hour: {i} tot time so far: {tot_time}')
    #             break
    #     else:    
    #         min_eating_count=min(i,min_eating_count)
            
    # return min_eating_count
    
    #binary search TC O(log n * n), SC O(1) where n=len(piles)
    low=1
    high=max(piles)
    min_eating_count=max(piles)

    while low<=high: #reduced the search space by binary search mechanism
        mid=(low+high)//2
        tot_time=0

        for pile in piles:
            tot_time+=ceil(pile/mid)
        if tot_time<=h:
            min_eating_count=mid
            high=mid-1
        else:
            low=mid+1

    return min_eating_count
        
     

test_cases = [
    ([3, 6, 7, 11], 8, 4),
    ([30, 11, 23, 4, 20], 5, 30),
    ([30, 11, 23, 4, 20], 6, 23),
    ([1, 1, 1, 1], 4, 1),
    ([312884470], 312884469, 2),
]

passed = 0

for i, (piles, h, expected) in enumerate(test_cases, 1):
    actual = minEatingSpeed(piles, h)

    if actual == expected:
        print(f"Test Case {i}: PASSED")
        passed += 1
    else:
        print(f"Test Case {i}: FAILED | Expected: {expected}, Got: {actual}")

print(f"\n{passed}/{len(test_cases)} PASSED")
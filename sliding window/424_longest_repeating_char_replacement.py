""""
LeetCode 424 — Longest Repeating Character Replacement

Basic explanation

Given a string s and an integer k, find the length of the longest substring 
you can make entirely of the same character by replacing at most k characters.


"""

def characterReplacement(s, k):
    #brute force approach TC O(N^2), SC O(count)
    # n=len(s)
    # max_length=0
    
    # for i in range(n):
    #     count=dict()
    #     max_freq=0
    #     for j in range(i,n):
    #         count[s[j]]=count.get(s[j],0) +1
    #         max_freq= max(max_freq,count[s[j]])
            
    #         curr_window=j-i+1
    #         remain_chars= curr_window-max_freq
    #         if remain_chars <= k:
    #             max_length=max(max_length,curr_window)
                
    # return max_length
    
    #optimal approach with slifing window TC O(n) SC O(count)
    n=len(s)
    left=0
    max_length=0
    max_freq=0
    count=dict()
    
    for right in range(n):
        count[s[right]]=count.get(s[right],0) +1 #every iteration lo char count track chei & max freq find chei
        
        max_freq=max(max_freq,count[s[right]])
        
        while right-left+1 - max_freq > k: #if right extralu chesthe left line lo pettudhi with left shrinking & char freq decrement
            count[s[left]]-=1
            left+=1
            
        max_length=max(max_length,right-left+1) #everytime must calculate 
        
    return max_length



# Main code
test_cases = [
    ("ABAB", 2, 4),
    ("AABABBA", 1, 4),
    ("AAAA", 2, 4),
    ("ABCDE", 1, 2),
    ("BAAAB", 2, 5)  # Tricky case
]

count: int = 0

for s, k, expected in test_cases:
    actual = characterReplacement(s, k)

    print("Input:   ", s)
    print("K:       ", k)
    print("Expected:", expected)
    print("Actual:  ", actual)
    print("Result:  ", "PASS" if actual == expected else "FAIL")
    print()

    if actual == expected:
        count += 1

print(f'{count}/{5} PASSED')
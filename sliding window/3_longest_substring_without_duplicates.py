"""

LeetCode 3 — Longest Substring Without Repeating Characters
Basic explanation
Given a string s, find the length of the longest substring without repeating characters.
A substring must contain consecutive characters.


"""

def lengthOfLongestSubstring(s):
    # Your code here
    n=len(s)
    if n<1:
        return 0
    
    left=0
    right=0
    seen={}
    max_window_size=0
    
    while right<n:
        #everytime char dict lo unte and left pointer duplicate char index cross ayyindha ledha check chei
        if s[right] in seen and seen[s[right]] >= left:
            left=seen[s[right]]+1
            
            
        #need update every iteration    
        seen[s[right]]=right  
        max_window_size=max(max_window_size,right-left+1)
        right+=1
        
    return max_window_size
            
            

# Main code
test_cases = [
    ("abcabcbb", 3),
    ("bbbbb", 1),
    ("pwwkew", 3),
    ("", 0),
    ("dvdf", 3)  # Tricky case  seen={d:2,v:1,f:3} m=2  3-1+1 
    #  l
    #    r
]

count: int = 0

for s, expected in test_cases:
    actual = lengthOfLongestSubstring(s)

    print("Input:   ", repr(s))
    print("Expected:", expected)
    print("Actual:  ", actual)
    print("Result:  ", "PASS" if actual == expected else "FAIL")
    print()

    if actual == expected:
        count += 1

print(f'{count}/{5} PASSED')


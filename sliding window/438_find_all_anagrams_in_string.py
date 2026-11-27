"""
LeetCode 438 – Find All Anagrams in a String
Difficulty: Medium

Problem: Given two strings s and p, return an array of all the start indices of p's anagrams in s.

An anagram is a rearrangement of the characters of a string.
"""


def findAnagrams(s, p):
    #brute force TC O(n-m), SC O(indexes)
    # n=len(s)
    # m=len(p)
    # sorted_p=sorted(p)
    # indexes=[]
    
    # for i in range(n-m+1):
    #     substring=s[i:i+m]
        
    #     if sorted(substring)==sorted_p:
    #         indexes.append(i)
            
    # return indexes

    #optimal appraoch slifing window TC O(n), SC O(indexes)
    n=len(s)
    m=len(p)
    left=0
    res=[]
    required=[0]*26
    for char in p:
        required[ord(char)-97] +=1
    
    window=[0]*26
    for right in range(n):
        index= ord(s[right])-97
        window[index]+=1
        
        while window[index]>required[index]: #to remove unwanted chars from window
            window[ord(s[left])-97]-=1
            left+=1
        
        if (right-left+1) == m:
            res.append(left)
            window[ord(s[left])-97]-=1
            left+=1
            
    return res       
    

test_cases = [
    ("cbaebabacd", "abc", [0, 6]),
    ("abab", "ab", [0, 1, 2]),
    ("aaaaaaaaaa", "aaaaa", [0, 1, 2, 3, 4, 5]),
    ("abc", "abcd", []),
    ("baa", "aa", [1]),
]

passed = 0

for i, (s, p, expected) in enumerate(test_cases, 1):
    actual = findAnagrams(s, p)

    if actual == expected:
        print(f"Test Case {i}: PASSED")
        passed += 1
    else:
        print(f"Test Case {i}: FAILED | Expected: {expected}, Got: {actual}")

print(f"\n{passed}/{len(test_cases)} PASSED")
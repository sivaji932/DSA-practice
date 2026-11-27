"""
LeetCode 242 
Valid Anagram
Difficulty: Easy

Problem: Given two strings s and t, return True if t is an anagram of s, and False otherwise.

An anagram is a word or phrase formed by rearranging the letters of another word or phrase, 
using all the original letters exactly once.

"""


from collections import Counter

def isAnagram(s1, s2):
    if len(s1)!=len(s2):
        return False
    
    count=Counter(s1)
    for char in s2:
        if char not in count:
            return False
        else:
            count[char] -= 1
            
    res=all(val==0 for val in count.values())
    return res


test_cases = [
    ("anagram", "nagaram", True),
    ("rat", "car", False),
    ("listen", "silent", True),
    ("a", "ab", False),
    ("aacc", "ccac", False),
]

passed = 0

for i, (s, t, expected) in enumerate(test_cases, 1):
    actual = isAnagram(s, t)

    if actual == expected:
        print(f"Test Case {i}: PASSED")
        passed += 1
    else:
        print(f"Test Case {i}: FAILED | Expected: {expected}, Got: {actual}")

print(f"\n{passed}/{len(test_cases)} PASSED")
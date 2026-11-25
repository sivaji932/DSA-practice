"""
LeetCode 709 To Lower Case
Difficulty: Easy

Problem: Given a string s, convert all uppercase English letters into lowercase
English letters and return the resulting string.
"""

def toLowerCase(s):
    ans=""
    
    for char in s:
        if  ord(char) >= 65 and ord(char) <= 90: #cap letter found
            lower= chr(ord(char)+32)
            ans+=lower
        else:
            ans+=char
        
        
    return ans


test_cases = [
    ("Hello", "hello"),
    ("here", "here"),
    ("LOVELY", "lovely"),
    ("Hello World", "hello world"),
    ("PyThOn123", "python123"),
]

passed = 0

for i, (s, expected) in enumerate(test_cases, 1):
    actual = toLowerCase(s)

    if actual == expected:
        print(f"Test Case {i}: PASSED")
        passed += 1
    else:
        print(f"Test Case {i}: FAILED | Expected: {expected}, Got: {actual}")

print(f"\n{passed}/{len(test_cases)} PASSED")
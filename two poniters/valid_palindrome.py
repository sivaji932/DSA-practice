"""
works only for alphabetic strings -Easy
"""

def is_palindrome(s):
    n = len(s)
    left =0
    right=n-1

    while left < right:
        if s[left].lower() != s[right].lower():
            return False
        
        left += 1
        right-=1

    return True




# Main code
test_cases = [
    ("madam", True),
    ("hello", False),
    ("Racecar", True),
    ("a", True),
    ("abba", True)
]

count: int = 0

for s, expected in test_cases:
    actual = is_palindrome(s)

    print("Input:   ", s)
    print("Expected:", expected)
    print("Actual:  ", actual)
    print("Result:  ", "PASS" if actual == expected else "FAIL")
    print()

    if actual == expected:
        count += 1

print(f'{count}/{5} PASSED')
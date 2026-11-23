
# """
# LeetCode 125 — Valid Palindrome
# """


def isPalindrome(s : str):
    n = len(s)
    left = 0
    right = n-1


    while left < right:
        if not s[left].isalnum():
            left += 1
        elif not s[right].isalnum():
            right -= 1
        elif s[left].lower() != s[right].lower():
            return False
        else:
            left += 1
            right -= 1

    return True


# Main code
test_cases = [
    ("A man, a plan, a canal: Panama", True),
    ("race a car", False),
    (" ", True),
    ("0P", False),
    ("Madam, I'm Adam", True),
    (".",True),
    ("a",True)
]

count: int = 0

for s, expected in test_cases:
    actual = isPalindrome(s)

    print("Input:   ", s)
    print("Expected:", expected)
    print("Actual:  ", actual)
    print("Result:  ", "PASS" if actual == expected else "FAIL")
    print()

    if actual == expected:
        count += 1

print(f'{count}/{7} PASSED')

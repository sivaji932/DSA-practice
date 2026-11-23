"""
LeetCode 11 — Container With Most Water
"""

def max_area(height):
    max_area_so_far=0
    n=len(height)

    for i in range(n):
        for j in range(i+1,n):
            current_area=(j-i)*min(height[i],height[j])
            max_area_so_far=max(current_area,max_area_so_far)

    return max_area_so_far


# Main code
test_cases = [
    ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
    ([1, 1], 1),
    ([4, 3, 2, 1, 4], 16),
    ([1, 2, 1], 2),
    ([2, 3, 10, 5, 7, 8, 9], 36)
]

count: int = 0

for height, expected in test_cases:
    actual = max_area(height)

    print("Input:   ", height)
    print("Expected:", expected)
    print("Actual:  ", actual)
    print("Result:  ", "PASS" if actual == expected else "FAIL")
    print()

    if actual == expected:
        count += 1

print(f'{count}/{5} PASSED')
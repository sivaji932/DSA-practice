"""
    Find the all contiguous subaray sums and find the largest prime number in that 
    sums
"""

from math import isqrt


def is_prime(num):
    if num <=1:
        return False
    
    if num <= 3: # 2 and 3 primes
        return True
    
    if num % 2 == 0 or num % 3 == 0:
        return False
    
    for i in range(5,isqrt(num)+1,6):
        if num % i == 0 or num % (i+2) == 0:
            return False
        
    return True


def max_sum_and_prime(arr):
    max_prime_so_far : int = -1
    n = len(arr)

    for i in range(n):
        for j in range(i+1,n+1):
            curr_sum = sum(arr[i:j])
            if is_prime(curr_sum):
                max_prime_so_far = max(max_prime_so_far,curr_sum)

    return max_prime_so_far
    


# Main code
test_cases = [
    ([1, 2, -1, 4, -2], 5),
    ([-2, 3, -1, 5, -4], 7),
    ([4, -10, 7, 2, -1], 7),
    ([-5, -3, -7, -2], -1),
    ([10, -5, 3, 4, -2, 11], 13)
]

count: int = 0

for arr, expected in test_cases:
    actual = max_sum_and_prime(arr)

    print("Input:   ", arr)
    print("Expected:", expected)
    print("Actual:  ", actual)
    print("Result:  ", "PASS" if actual == expected else "FAIL")
    print()

    if actual == expected:
        count += 1

print(f'{count}/{5} PASSED')
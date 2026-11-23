"""
leetcode 53

"""

# quick remember

# at every element either extend the subarray or start a new sub array (kadane's algorithm)



def max_subarray_sum(arr):
    #brute force  TC O(n^2) , SC (n)
    # n=len(arr)
    # max_sum=float('-inf')
    
    # for i in range(n):
    #     curr_sum=0
    #     for j in range(i,n):
    #         curr_sum+=arr[j]
    #         max_sum=max(max_sum,curr_sum)
              
    # return max_sum
    
    #optimal approach (kadane's algorithm)  TC O(n) , SC O(1)
    n=len(arr)
    max_sum=arr[0]
    curr_sum=arr[0]
    
    for i in range(1,n):
        if curr_sum>=0:
            curr_sum+=arr[i]
        else:
            curr_sum=arr[i]
            
        max_sum=max(max_sum,curr_sum)
    
    return max_sum        
    
    
# Main code
test_cases = [
    ([1, 2, 3, 4], 10),
    ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
    ([-5, -2, -8, -1], -1),
    ([5], 5),                    # single element
    ([8, -10, 3, 4, -1, 2], 8) # tricky case
]

count : int = 0

for arr, expected in test_cases:
    actual = max_subarray_sum(arr)

    print("Input:   ", arr)
    print("Expected:", expected)
    print("Actual:  ", actual)
    print("Result:  ", "PASS" if actual == expected else "FAIL")
    print()
    if actual == expected:
        count += 1

print(f'{count}/{5} PASSED')
"""


LeetCode 238 — Product of Array Except Self


You are given an integer array nums. Return an array answer such that answer[i]
is equal to the product of all elements in nums except nums[i] itself.

Example
Input:  nums = [1, 2, 3, 4] Output: [24, 12, 8, 6]


Explanation:
- Index 0: \(2 \times 3 \times 4 = 24\)
- Index 1: \(1 \times 3 \times 4 = 12\)
- Index 2: \(1 \times 2 \times 4 = 8\)
- Index 3: \(1 \times 2 \times 3 = 6\)
Each output element is the product of every other element, excluding the element at the same index.

"""


def productExceptSelf(nums):
    # brute force O(n^2)
    # res = []
    # n = len(nums)

    # for i in range(n):
    #     prod = 1
    #     for j in range(n):
    #         if i != j:
    #             prod = prod * nums[j]
    #     res.append(prod)

    # return res


    #better approach O(n) T.C
    n = len(nums)
    prefix_prod = [nums[0]]
    suffix_prod = [0] * n
    suffix_prod[n-1] = nums[n-1]
    ans = [0] * n

    for i in range(1,n):
        prefix_prod.append(prefix_prod[i-1] * nums[i])

    for i in range(n-2,-1,-1):
        suffix_prod[i] = suffix_prod[i+1] * nums[i]

    ans[0] = suffix_prod[1]  # First element's answer is the product of all elements to its right

    for i in range(1,n-1):
        ans[i] = prefix_prod[i-1] * suffix_prod[i+1]

    ans[n-1] = prefix_prod[n-2]

    return ans

# Main code
test_cases = [
    ([1, 2, 3, 4], [24, 12, 8, 6]),
    ([-1, 1, 0, -3, 3], [0, 0, 9, 0, 0]),
    ([2, 3], [3, 2]),
    ([1, 1, 1, 1], [1, 1, 1, 1]),
    ([0, 2, 3, 4], [24, 0, 0, 0])   # edge case
]

count: int = 0

for nums, expected in test_cases:
    actual = productExceptSelf(nums)

    print("Input:   ", nums)
    print("Expected:", expected)
    print("Actual:  ", actual)
    print("Result:  ", "PASS" if actual == expected else "FAIL")
    print()

    if actual == expected:
        count += 1

print(f'{count}/{5} PASSED')


""" 

### Dry Run

Input: `nums = [1, 2, 3, 4]`

Step 1: Initialization

```
prefix_prod = [1]  suffix_prod = [0, 0, 0, 4]  ans = [0, 0, 0, 0]
```

Step 2: Calculate prefix products

Each element stores the product of all elements from index `0` to `i`.

| `i` | Calculation  | `prefix_prod`   |
| --- | ------------ | --------------- |
| 1   | `1 * 2 = 2`  | `[1, 2]`        |
| 2   | `2 * 3 = 6`  | `[1, 2, 6]`     |
| 3   | `6 * 4 = 24` | `[1, 2, 6, 24]` |

Step 3: Calculate suffix products

Each element stores the product of all elements from index `i` to the last index.

| `i` | Calculation   | `suffix_prod`     |
| --- | ------------- | ----------------- |
| 2   | `4 * 3 = 12`  | `[0, 0, 12, 4]`   |
| 1   | `12 * 2 = 24` | `[0, 24, 12, 4]`  |
| 0   | `24 * 1 = 24` | `[24, 24, 12, 4]` |

Step 4: Build the answer array

- `ans[0] = suffix_prod[1] = 24`
- `ans[1] = prefix_prod[0] * suffix_prod[2] = 1 * 12 = 12`
- `ans[2] = prefix_prod[1] * suffix_prod[3] = 2 * 4 = 8`
- `ans[3] = prefix_prod[2] = 6`

Final output:

```
ans = [24, 12, 8, 6]
```


"""
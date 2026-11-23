
# LeetCode 303 — Range Sum Query - Immutable



class NumArray:
    

    def __init__(self, nums):
        if not nums:
            self.prefix_sum = []
            return
        
        # calculate prefix sum right here
        self.prefix_sum = [nums[0]]
        for i in range(1,len(nums)):
            self.prefix_sum.append(self.prefix_sum[i-1] + nums[i])

    def sumRange(self, left, right):
        if left == 0:
            return self.prefix_sum[right]
        
        return self.prefix_sum[right] - self.prefix_sum[left-1]
        


# Main code
test_cases = [
    ([-2, 0, 3, -5, 2, -1], [(0, 2, 1), (2, 5, -1), (0, 5, -3)]),
    ([1, 2, 3, 4, 5], [(0, 4, 15), (1, 3, 9)]),
    ([5], [(0, 0, 5)]),
    ([-5, -2, -3], [(0, 2, -10), (1, 2, -5)]),
    ([10, -10, 20, -5], [(0, 1, 0), (1, 3, 5)])
]

count: int = 0
total: int = 0

for nums, queries in test_cases:
    obj = NumArray(nums)

    for left, right, expected in queries:
        actual = obj.sumRange(left, right)

        print("Input:   ", nums)
        print("Range:   ", (left, right))
        print("Expected:", expected)
        print("Actual:  ", actual)
        print("Result:  ", "PASS" if actual == expected else "FAIL")
        print()

        total += 1

        if actual == expected:
            count += 1

print(f'{count}/{total} PASSED')
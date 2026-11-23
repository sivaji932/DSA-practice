"""
Docstring for greedy.121_best_time_to_sell_stock
"""



def maxProfit(prices):
    #brute force approach TC O(n^2), SC O(1)
    # n=len(prices)
    # max_profit=0
    
    # for i in range(n):
    #     for j in range(i+1,n):
    #         curr_profit=prices[j]-prices[i]
    #         max_profit=max(max_profit,curr_profit)
            
    # return max_profit
    
    #optimal approach with greedy TC O(n), Sc O(1)
    n=len(prices)
    max_profit=0
    min_price=float('inf')
    
    for i in range(n):
        if prices[i]<min_price:
            min_price=prices[i]
        else:
            curr_profit=prices[i]-min_price
            max_profit=max(max_profit,curr_profit)
            
    return max_profit



test_cases = [
    ([7, 1, 5, 3, 6, 4], 5),
    ([7, 6, 4, 3, 1], 0),
    ([2, 4, 1], 2),
    ([1, 5], 4),
    ([3, 2], 0)
]

count: int = 0

for prices, expected in test_cases:
    actual = maxProfit(prices)
    status = "PASS" if actual == expected else "FAIL"

    print(f"{status}: expected={expected}, actual={actual}")

    if actual == expected:
        count += 1

print(f"{count}/5 PASSED")

"""
LeetCode 904 — Fruit Into Baskets

Basic explanation

You are given an array fruits, where each number represents a fruit type.
You have 2 baskets, and each basket can hold only one fruit type. Find the 
maximum number of fruits you can collect from a contiguous subarray containing at most 2 
distinct types.

"""


def totalFruit(fruits):
    #brute force TC-O(n^2) SC-O(collected_fruits)
    # n=len(fruits)
    # max_window=0
    
    # for i in range(n):
    #     collected_fruits=set()
    #     curr_window=0
    #     for j in range(i,n):
    #         if fruits[j] not in collected_fruits: #everytime new fruit basket lo add chei
    #             collected_fruits.add(fruits[j])
                
    #         if len(collected_fruits)>2: #okavelka basket lo 2 fruits kanna ekkuva unte inka iteration apei
    #             break
    #         curr_window+=1
            
    #     if curr_window>max_window:
    #         max_window=curr_window
            
    # return max_window
    
    
    #better approach TC - O(n) SC - O(search_space)
    n=len(fruits)
    left=0
    right=0
    search_space=dict()
    max_window=0
    
    while right<n:
        #prathisari fruit count modify ledha new fruit add chei   
        search_space[fruits[right]] = search_space.get(fruits[right],0)+1
            
        if len(search_space)>2: #okavela right ekkuvachesthe left sarichesthundhi
            while len(search_space)>2:
                search_space[fruits[left]] -= 1
                if search_space[fruits[left]]==0:
                    del search_space[fruits[left]]
                left+=1
               
        max_window=max(max_window,right-left+1) 
        right+=1
        
        
    return max_window
        
    
         
# Main code
test_cases = [
    ([1, 2, 1], 3),
    ([0, 1, 2, 2], 3),
    ([1, 2, 3, 2, 2], 4),
    ([1, 1, 1, 1], 4),
    ([1, 2, 3, 4, 5], 2)  # Edge case
]

count: int = 0

for fruits, expected in test_cases:
    actual = totalFruit(fruits)

    print("Input:   ", fruits)
    print("Expected:", expected)
    print("Actual:  ", actual)
    print("Result:  ", "PASS" if actual == expected else "FAIL")
    print()

    if actual == expected:
        count += 1

print(f'{count}/{5} PASSED')
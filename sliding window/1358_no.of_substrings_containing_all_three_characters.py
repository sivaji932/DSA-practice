""""

LeetCode 1358 — Number of Substrings Containing All Three Characters

Basic explanation
Given a string s containing only 'a', 'b', and 'c', count the number of substrings that contain
at least one occurrence of all three characters.


"""
#aabc,aabcb,aabcbc  abc,abcb,abcbc  

def numberOfSubstrings(s):
    #brute force TC (n^2) SC O(search_space)
    # n=len(s)
    # count=0
    
    # for i in range(n-2):
    #     search_space=[0,0,0]
    #     for j in range(i,n):
    #         if s[j] not in search_space:
    #             search_space[ord(s[j]) - ord('a')]=1
                
    #         if sum(search_space)==3:
    #             count+=1
            
    # return count

    #better approach - we reduced some iterations but still O(n^2) TC at worst case SC O(search_space)
    # n=len(s)
    # count=0
    
    # for i in range(n-2):
    #     search_space=[0,0,0]
    #     for j in range(i,n):
    #         search_space[ord(s[j]) - ord('a')]=1
                
    #         if sum(search_space)==3:
    #             count+=(n-j)  #nuvvu inka right side lo under answers skip cheyyi becoz no need to iterate (range-)
    #             break
            
    # return count
    
    #optimal approach TC O(n) , SC O(search_space)
    n=len(s)
    count=0
    right=0
    search_space=[-1,-1,-1] #opposite logic to better approach ante left unna possible combos vatilni min index tho rappisthav
    
    while right<n:
        search_space[ord(s[right]) - ord('a')]=right
        
        if search_space[0] != -1 and search_space[1] != -1 and search_space[2] != -1:
            min_index=min(search_space) #min index tiskuni +1 add chestav then all left possible combos count vastundhi
            count+= min_index+1

        right+=1
            
    return count
        

    

# Main code
test_cases = [
    ("abcabc", 10),
    ("aaacb", 3),
    ("abc", 1),
    ("aaaa", 0),
    ("aabcbc", 6)
]

count: int = 0

for s, expected in test_cases:
    actual = numberOfSubstrings(s)

    print("Input:   ", s)
    print("Expected:", expected)
    print("Actual:  ", actual)
    print("Result:  ", "PASS" if actual == expected else "FAIL")
    print()

    if actual == expected:
        count += 1

print(f'{count}/{5} PASSED')
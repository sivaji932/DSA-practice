def subarray_sum(nums,k):
    n=len(nums)
    
    if k<=0 or k>n:
        return None
    
    window_sum=max_sum=sum(nums[:k]) #precalculated first window sum
    i=1 #and started with second window
    j=k
    
    while j<n:
        window_sum+=nums[j]
        window_sum-=nums[i-1]

        max_sum=max(window_sum,max_sum)
        
        i+=1
        j+=1
        
    return max_sum


print(subarray_sum([2,1,5,1,3,2],3))

"""

2,1,5 = 8 sum 1
    8+1=9
    9-2=7
    1,5,1=7 sum 2
        7+3=10
        10-1=9
        5,1,3=9 sum 3 -> max sum
        9+2=11
        11-5=6
        1,3,2=6 sum 4


"""
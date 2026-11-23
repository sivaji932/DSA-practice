def subarray_sum_less_than_k(nums,k): #k means target value
    n=len(nums)
    i=0
    j=0
    max_window_size=0
    window_sum=0
    
    while j<n:
        window_sum+=nums[j]
        
        if window_sum>=k:
            window_sum-=nums[i]
            i+=1
            
        if window_sum<k:
            max_window_size=max(j-i+1,max_window_size)  
        
        j+=1 
            
    return max_window_size


print(subarray_sum_less_than_k([2,1,3,2,1,1,1],6)) # 4

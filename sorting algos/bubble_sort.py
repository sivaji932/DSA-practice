"""

bubble sort 

"""
def bubbleSort(nums):
    n=len(nums)
    
    for i in range(n-1):
        swapped=False
        for j in range(n-i-1): #becoz we have to skip sorted elements at end
            if nums[j]>nums[j+1]:
                nums[j], nums[j+1]= nums[j+1],nums[j]
                swapped=True
                
        if not swapped: #current pass lo emi swap avvakapothe array already sorted so skip process
            break
        
    return nums


if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, -1,-1,0, 90]

    bubbleSort(arr)

    print("Sorted array:")
    for i in range(len(arr)):
        print("%d" % arr[i], end=" ")
l=[1,2,3,4,5,6,7,8,9]
n=len(l)


#use slicing
# print(l[::-1])

#use reversed() ,most efficent way
for num in reversed(l):
    print(num,end=" ")

#use reverse() -> inplace modification so input changes remember
# l.reverse()
# print(l)

#just reverse iteration
#              start  stop   step
# for i in range(n-1  , -1  , -1):
#     print(i,l[i],end="\n")

#just reverse indexing iteration
# for i in range(-1,((n+1)*-1),-1):
#     print(i,l[i],end="\n")


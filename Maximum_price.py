def MaxCoinsPossible(nums):#main logic compuation function returns the maxcoinspossible
    nums = [1]+nums+[1]
    size = len(nums)
    dynamicarray = [[0]*size for _ in range(size)]
    for p in range(size-1,-1,-1):
        for q in range(p+1,size):
            for k in range(p+1,q):
                dynamicarray[p][q] = max(dynamicarray[p][q], max(dynamicarray[p][k]+dynamicarray[k][q]+nums[q]*nums[q]+nums[k],dynamicarray[p][k]+dynamicarray[k][q]+nums[p]+nums[q]*nums[k]))
    return dynamicarray[0][size-1]
length=int(input())   #reading no_of opponents
opponents=list(map(int,input().split()))
print(MaxCoinsPossible(opponents)-2,end="")   #final result maxcoinspossible

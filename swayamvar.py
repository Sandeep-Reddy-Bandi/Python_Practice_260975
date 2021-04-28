n=int(input())#taking input no'of pairs in swayamvar
l1=list(input())#grooms
l2=list(input())#brides
for i in l1:#traverse through the grooms list
    if i in l2 :#if that particular drink is avaliable in brides list
        l2.remove(i)#they they both are pairs
    else:
        break#else no other get marriad
print(len(l2),end="")#finally remaining pairs will be in brides list


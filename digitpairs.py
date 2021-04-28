def combination(l):
    return list(combinations(l, 2))  # list of all possible pairs


from itertools import combinations

n = int(input())  # taking n value
l = list(map(str, input().split()))  # reading an array of values
update = []
for num in l:
    update.append(
        str((int(max(list(num))) * 11) + (int(min(list(num))) * 7))[-2:])  # hahah niku ardham avvadhule cudaku
c = 0
even = []  # creating even indices values
odd = []  # creating odd indices values
for i in update:
    if c == 0:
        odd.append(i)
        c = 1
    else:
        even.append(i)
        c = 0

evenpairs = combination(even)  # calling combination function for list of all possible pairs
oddpairs = combination(odd)  # calling combination function for list of all possible pairs
d = dict()  # creating a dictionary of the pairs
for x in evenpairs:  # checking for equal most significant bits in even pairs
    if x[0][0] == x[1][0]:
        if x[0][0] in d:
            d[x[0][0]] += 1;
        else:
            d[x[0][0]] = 1

for x in oddpairs:  # checking for most significant bits in odd pairs
    if x[0][0] == x[1][0]:
        if x[0][0] in d:
            d[x[0][0]] += 1;
        else:
            d[x[0][0]] = 1
ans = 0
for x in d:  # traverse in the dictionary for final checking for atmost 2 significant bits.
    if d[x] > 2:
        ans += 2
    else:
        ans += d[x]
print(ans, end="")

n = int(input())
arr = list(map(int, input().split()))
l = []
l.append([0, 0])

t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    f = 0
    for a in l:
        if x in a and len(a) < t:
            a.append(y)
            f = 1
            break
        elif y in a and len(a) < t:
            a.append(x)
            f = 1
            break
    if f == 0:
        l.append([x, y])

l.remove([0, 0])

empty = []
for i in range(1, n + 1):
    empty.append(i)

for a in l:
    for i in a:
        if i in empty:
            empty.remove(i)
l.append(empty)

for i in range(0, len(l)):
    l[i] = list(set(l[i]))
l = sorted(l, key=lambda ele: len(ele), reverse=True)

m = 0
res = []
for a in l:
    s = 0
    for i in a:
        s += arr[i - 1]

    if m <= s:
        res = a
        m = s
for i in range(len(res) - 1):
    print(res[i], end=" ")
print(res[len(res) - 1], end="")


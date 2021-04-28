t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    val = []
    for i in range(97, 97 + n):
        val.append(chr(i))
    x = [0] * n
    z = val.copy()
    c = 0

    for i in range(0, 100000000):
        c += 1
        for i in range(0, n):
            x[l[i] - 1] = z[i]
        z = x.copy()
        if z == val:
            print(c, end="")
            break



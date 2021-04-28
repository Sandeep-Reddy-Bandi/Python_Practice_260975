def fun(x, y):
    c = 0
    while (x > 0 and y > 0):
        c += 1
        if (x > y):
            x = x - y
        else:
            y = y - x
    return c


a = int(input())
b = int(input())
c = int(input())
d = int(input())
ans = 0

for i in range(a, b + 1):
    for j in range(c, d + 1):
        ans += c
print(ans, end="")






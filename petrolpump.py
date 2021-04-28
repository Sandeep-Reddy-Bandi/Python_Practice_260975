def dpsubset(arr, n, s):
    dp = []
    for i in range(0, n + 1):
        dp.append([0] * (s + 1))
    for i in range(0, n + 1):
        for j in range(0, s + 1):
            if i == 0:
                dp[i][j] = 0
            if j == 0:
                dp[i][j] = 1
    for i in range(1, n + 1):
        for j in range(1, s + 1):
            if (arr[i - 1] <= j):
                dp[i][j] = (dp[i - 1][j - arr[i - 1]]) or dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j]
    m1 = 0

    for i in range(s // 2, -1, -1):
        if dp[n][i] == 1:
            m1 = s - i
            break

    return m1


l = list(map(int, input().split()))
print(dpsubset(l, len(l), sum(l)), end="")

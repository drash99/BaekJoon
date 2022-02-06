n, k = map(int, input().split())

dp = dict()

def finddp(i):
    if i in dp.keys():
        return dp[i]
    return 0

for i in range(n+1):
    dp[(i,0)] = 1

for i in range(1,k):
    for j in range(n+1):
        for l in range(n+1):
            dp[(j+l, i)] = finddp((l,i-1)) + finddp((j+l,i))


print(dp[(n,k-1)]%1000000000)
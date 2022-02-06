t = int(input())

dp = dict()

def finddp(i):
    if i in dp.keys():
        return dp[i]
    return 0

dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, 1000001):
    dp[i] = (dp[i-1]+dp[i-2]+dp[i-3])%1000000009

for i in range(t):
    n = int(input())
    print(finddp(n))

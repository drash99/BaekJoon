import sys

N = int(input())

dp = dict()

def finddp(i):
    if i in dp.keys():
        return dp[i]
    else:
        return 0

prices = []

for i in range(N):
    prices.append(tuple(map(int, sys.stdin.readline().split())))

for i in range(N-1, -1, -1):
    if i+prices[i][0] > N:
        dp[i] = finddp(i+1)
    else:
        prev = finddp(i+1)
        curr = prices[i][1] + finddp(i+prices[i][0])
        dp[i] = max(prev,curr)

print(dp[0])
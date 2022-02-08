n = int(input())
wines = []

for i in range(n):
    wines.append(int(input()))

dp = dict()

def finddp(i):
    if i in dp.keys():
        return dp[i]
    return 0

for i in range(n):
    dp[(i,0)] = max(finddp((i-1,0)), finddp((i-1,1)), finddp((i-1,2)))
    dp[(i,1)] = wines[i] + finddp((i-1,0))
    dp[(i,2)] = wines[i] + finddp((i-1,1))

print(max(finddp((n-1,0)),finddp((n-1,1)),finddp((n-1,2))))
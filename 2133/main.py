n = int(input())

dp = dict()

def finddp(i):
    if i in dp.keys():
        return dp[i]
    return 0

dp[(1,0)] = 1
for i in range(2,n+2):
    dp[(i,0)] = finddp((i-2,11)) + finddp((i-2,110)) + 3*finddp((i-2,0))
    dp[(i,1)] = finddp((i-1,0)) + finddp((i-1,110))
    dp[(i,100)] = finddp((i-1,0)) + finddp((i-1,11))
    dp[(i,110)] = finddp((i-1,1))
    dp[(i,11)] = finddp((i-1,100))

print(finddp((n+1,0)))
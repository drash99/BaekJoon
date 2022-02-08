n = int(input())
dp = dict()
def finddp(i):
    if i in dp.keys():
        return dp[i]
    return 0

data = []
for i in range(n):
    data.append(tuple(map(int, input().split())))


dp[(1,0)] = data[0][0]
dp[(1,1)] = data[0][1]
dp[(1,2)] = data[0][2]

for i in range(2, n+1):
    dp[(i,0)] = min(finddp((i-1,1)),finddp((i-1,2)))+data[i-1][0]
    dp[(i,1)] = min(finddp((i-1,0)),finddp((i-1,2)))+data[i-1][1]
    dp[(i,2)] = min(finddp((i-1,1)) , finddp((i-1,0)))+data[i-1][2]

print(min(finddp((n,0)),finddp((n,1)),finddp((n,2))))
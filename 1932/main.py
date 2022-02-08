n = int(input())

tri = []

for i in range(n):
    tri.append(list(map(int, input().split())))

dp = dict()

def finddp(i):
    if i in dp.keys():
        return dp[i]
    return 0

for i in range(n):
    for j in range(i+1):
        dp[(i,j)] = tri[i][j]+ max(finddp((i-1,j-1)), finddp((i-1,j)))

ans = 0
for i in range(n):
    ans = max(ans, finddp((n-1, i)))

print(ans)
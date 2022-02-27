n = int(input())


dp = [[-1 for _ in range(n+1)] for _ in range(n+1)]

rawins = []
for _ in range(n):
    rawins.append(list(map(int, input().split())))



ans=0

#print(brands, newbrands)

def solve(i,j):
    #print(i,j)
    if j<=i+1:
        return 0
    if dp[i][j] != -1:
        return dp[i][j]

    dp[i][j] = solve(i+1,j)
    
    for a in range(i+1,j):
        if rawins[i][a] == 1:
            dp[i][j] = max(dp[i][j], solve(i+1,a) + solve(a+1, j) + 1)
    return dp[i][j]

print(ans+solve(0,n))

n, m = map(int, input().split())
lights= []
inf = 2147483647
for _ in range(n):
    lights.append(tuple(map(int, input().split())))

p = lights[m-1][0]
lights.sort()
dp = [[[-1,-1] for _ in range(n)] for _ in range(n)]
start = 0
for idx, light in enumerate(lights):
    if light[0] == p:
        start = idx
def findsum(l,r):
    ans =0
    for i in range(l):
        ans +=lights[i][1]
    for j in range(r+1,len(lights)):
        ans += lights[j][1]
    return ans

def solve(l,r,dire):
    #print(l,r,dire)
    if l < 0 or r >= len(lights):
        return inf
    if dp[l][r][dire] != -1:
        return dp[l][r][dire]
    if l == 0 and r == len(lights)-1:
        dp[l][r][dire] = 0
        #print(l,r, 0)
        return 0
    ans = inf
    if dire==0:
        if l>0:
            ans = min(ans, solve(l-1,r, 0)+(findsum(l,r))*(lights[l][0]-lights[l-1][0]))
        if r < n-1:
            a = solve(l,r+1,1)+(findsum(l,r))*(lights[r+1][0]-lights[l][0])
        #print(a, findsum(l,r))
            ans = min(ans, a)
    if dire==1:
        if r<len(lights)-1:
            a = solve(l,r+1,1)+(findsum(l,r))*(lights[r+1][0]-lights[r][0])
            ans = min(ans, a)
        if l > 0:
            ans = min(ans, solve(l-1,r, 0)+(findsum(l,r))*(lights[r][0]-lights[l-1][0]))
    dp[l][r][dire] = ans
    #print(l,r, dire, ans)
    return ans

#print(lights)
print(solve(start,start,0))